from django.shortcuts import render
from .models import Meme, Comment
from django.core.paginator import Paginator
from django.views.generic import (TemplateView, 
                                  ListView, 
                                  DetailView, 
                                  CreateView, 
                                  UpdateView,
                                  DeleteView)
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import CommentRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse

class MemeListView(ListView):
    template_name = 'memopolis/index.html'
    
    def get_context_data(self, **kwargs):
        context = {}

        if self.template_name == 'memopolis/index.html':
            tops = Meme.objects.order_by('-num_vote_up')[:3]
            
            context['tops']=tops

        return context
    
    def get(self, request):
        context = self.get_context_data()
        template = self.template_name
        
        if self.template_name == 'memopolis/index.html':
            meme_list = Meme.objects.order_by('-date_posted').filter(accepted=True)
        elif self.template_name == 'memopolis/top.html':
            meme_list = Meme.objects.order_by('-num_vote_up').filter(accepted=True)
        elif self.template_name == 'memopolis/unaccepted_memes.html':
            meme_list = Meme.objects.order_by("-date_posted").filter(accepted=False)
            
        for meme in meme_list:
            meme.if_user_upvoted = meme.votes.exists(request.user.id, action=0)
            meme.if_user_downvoted = meme.votes.exists(request.user.id, action=1)        
            
        paginator = Paginator(meme_list, 2)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj

        return render(request, template, context)
        
class TopMemeListView(MemeListView):
    template_name = 'memopolis/top.html'
    
    def get_context_data(self, **kwargs):
        context = {}
        if self.template_name == 'memopolis/top.html':
            memes = Meme.objects.order_by('-num_vote_up').filter(accepted=True)
            context['memes']=memes
        else:
            context = super().get_context_data(**kwargs)
        return context
    
class UnacceptedMemeListView(MemeListView):
    template_name = 'memopolis/unaccepted_memes.html'
    
    def get_context_data(self, **kwargs):
        context = {}
        memes = Meme.objects.order_by("-date_posted").filter(accepted=False)
        context['memes']=memes
        
        return context
    
class MemeDetailView(DetailView):
    model = Meme
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meme = context['meme']
        comments = Comment.objects.filter(belongs_to=meme)
        context['comments'] = comments
        
        form = CommentRegisterForm()
        context['form'] = form
        
        meme.if_user_upvoted = meme.votes.exists(self.request.user.id, action=0)
        meme.if_user_downvoted= meme.votes.exists(self.request.user.id, action=1)
        
        for comment in comments:
            comment.if_user_upvoted = comment.votes.exists(self.request.user.id, action=0)
            comment.if_user_downvoted = comment.votes.exists(self.request.user.id, action=1)
        
        return context
    
class MemeCreateView(CreateView):
    model = Meme
    fields = ['title','image','tags']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class MemeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Meme
    fields = ['title','tags']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        meme = self.get_object()
        if self.request.user == meme.author:
            return True
        return False
    
class YourMemesListView(ListView):
    template_name = 'memopolis/your_memes.html'
    
    def get(self, request):
        template=self.template_name
        memes = Meme.objects.filter(author=request.user.id).order_by('-date_posted')

        context = {}
        
        paginator = Paginator(memes, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        
        return render(request, template, context)

class YourPointsView(TemplateView):
    template_name = 'memopolis/your_points.html'

    def get(self, request):
        template=self.template_name
        
        context = {}
        
        memes = Meme.objects.filter(author=request.user.id).order_by('-num_vote_up')[:5]
        context['memes'] = memes
        


        context['js_memes'] = Meme.objects.values()
        
        like_sum = 0
        dislike_sum = 0
        all_memes = Meme.objects.filter(author=request.user.id)
        for meme in all_memes:
            like_sum+=meme.num_vote_up
        for meme in all_memes:
            dislike_sum+=meme.num_vote_down
        context['like_sum']=like_sum
        context['dislike_sum']=dislike_sum
        
        js_meme_titles = [meme.title for meme in memes]
        import json
        js_meme_titles = json.dumps(js_meme_titles)
        context['js_meme_titles'] = js_meme_titles
        
        js_meme_likes = [meme.num_vote_up for meme in memes]
        js_meme_dislikes = [meme.num_vote_down for meme in memes]
        #import json
        context['js_meme_likes'] = json.dumps(js_meme_likes)
        context['js_meme_dislikes'] = json.dumps(js_meme_dislikes)
        
        return render(request, template, context)
   
class MemeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Meme
    success_url = '/'
    
    def test_func(self):
        meme = self.get_object()
        if self.request.user == meme.author or self.request.user.is_superuser:
            return True
        return False

def post_vote(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        
        object_pk = request.POST["object_pk"]
        user_id = request.POST["user_id"]
        what_to_do = request.POST["what_to_do"]
        direction = request.POST["direction"]



        
        if direction == 'meme':
            meme = Meme.objects.get(pk=object_pk)
            if what_to_do == 'up':
                if meme.votes.exists(user_id, action=0):
                    meme.votes.delete(user_id)
                    meme.num_vote_up-=1
                elif meme.votes.exists(user_id, action=1):
                    meme.votes.delete(user_id)
                    meme.num_vote_down-=1
                    meme.votes.up(user_id)
                    meme.num_vote_up+=1
                else:
                    meme.votes.up(user_id)
                    meme.num_vote_up+=1
                    
            elif what_to_do == 'down':
                if meme.votes.exists(user_id, action=0):
                    meme.votes.delete(user_id)
                    meme.num_vote_up-=1
                    meme.votes.down(user_id)
                    meme.num_vote_down+=1
                elif meme.votes.exists(user_id, action=1):
                    meme.votes.delete(user_id)
                    meme.num_vote_down-=1
                else:
                    meme.votes.down(user_id)
                    meme.num_vote_down+=1
            meme.save()
            
        elif direction == 'comment':
            comment = Comment.objects.get(pk=object_pk)
            if what_to_do == 'up':
                if comment.votes.exists(user_id, action=0):
                    comment.votes.delete(user_id)
                    comment.num_vote_up-=1
                elif comment.votes.exists(user_id, action=1):
                    comment.votes.delete(user_id)
                    comment.num_vote_down-=1
                    comment.votes.up(user_id)
                    comment.num_vote_up+=1
                else:
                    comment.votes.up(user_id)
                    comment.num_vote_up+=1
                    
            elif what_to_do == 'down':
                if comment.votes.exists(user_id, action=0):
                    comment.votes.delete(user_id)
                    comment.num_vote_up-=1
                    comment.votes.down(user_id)
                    comment.num_vote_down+=1
                elif comment.votes.exists(user_id, action=1):
                    comment.votes.delete(user_id)
                    comment.num_vote_down-=1
                else:
                    comment.votes.down(user_id)
                    comment.num_vote_down+=1    
            comment.save()       
        
        else:
            print('direction error')


        # send to client side.
        return JsonResponse({}, status=200)

    # some error occured
    return JsonResponse({"error": ""}, status=400)

def post_comment(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        
        content = request.POST['content']
        direction = request.POST['direction']
        meme_pk = request.POST['meme-pk']
        meme = Meme.objects.get(pk=meme_pk)
        
        if direction == 'create-comment':
            comment = Comment()

            comment.content = content
            comment.author = request.user

            comment.belongs_to = meme
            
            
            
            comment.save()

        # send to client side.
        return JsonResponse({}, status=200)

    # some error occured
    return JsonResponse({"error": ""}, status=400)

def delete_comment(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        
        direction = request.POST['direction']
        object_pk = request.POST['object_pk']
        
        if direction == 'delete-comment':
            comment = Comment.objects.get(pk=object_pk)

            comment.delete()

        # send to client side.
        return JsonResponse({}, status=200)

    # some error occured
    return JsonResponse({"error": ""}, status=400)

def kontakt(request):
    return render(request, 'memopolis/kontakt.html')
