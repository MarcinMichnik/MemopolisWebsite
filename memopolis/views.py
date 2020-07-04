from django.shortcuts import render
from .models import Meme, Comment
from django.core.paginator import Paginator
from django.views.generic import (TemplateView, 
                                  ListView, 
                                  DetailView, 
                                  CreateView, 
                                  UpdateView)
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import CommentRegisterForm

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
            
        paginator = Paginator(meme_list, 2)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj

        return render(request, template, context)

    def post(self, request):
        
        raw = list(request.POST)[1]
        print(raw)
        raw = raw.split(' ')
        
        object_pk, user_id, vote = raw[0], raw[1], raw[2]

        
        meme = Meme.objects.get(pk=object_pk)
        
        if vote == "up":
            if meme.votes.exists(user_id):
                meme.votes.delete(user_id)
                meme.num_vote_up-=1
            else:
                meme.votes.up(user_id)
                meme.num_vote_up+=1
        
        
        
        meme.save()
        
        return HttpResponseRedirect("")
        
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

        return context

        

    
    def post(self, request, *args, **kwargs):
        
        raw = request.POST
        
        
        if list(raw)[1]!='content':
            raw = list(request.POST)[1]
            raw = raw.split(' ')
            print(raw)
            object_pk, user_id, vote, direction = raw[0], raw[1], raw[2], raw[3]

        else:
            raw = request.POST['content']
            direction='create_comment'
        
        if direction == 'meme':
            print('s')
            meme = Meme.objects.get(pk=object_pk)
            
            if vote == 'up':
                if meme.votes.exists(user_id):
                    meme.votes.delete(user_id)
                    meme.num_vote_up-=1
                else:
                    meme.votes.up(user_id)
                    meme.num_vote_up+=1
            meme.save()
        elif direction == 'comment':
            comment = Comment.objects.get(pk=object_pk)
            if vote == 'up':
                if comment.votes.exists(user_id):
                    comment.votes.delete(user_id)
                    comment.num_vote_up-=1
                else:
                    comment.votes.up(user_id)
                    comment.num_vote_up+=1
            comment.save()
            
        elif direction == 'create_comment':
            comment = Comment()

            comment.content = raw
            comment.author=request.user
            print(comment)
            self.object = self.get_object()
            context = self.get_context_data()

            comment.belongs_to = context['meme']
            
            
            comment.save()
        return HttpResponseRedirect('')
    
class MemeCreateView(CreateView):
    model = Meme
    fields = ['title','image','tags']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class MemeUpdateView(UpdateView):
    model = Meme
    fields = ['title','tags']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class YourMemesListView(ListView):
    template_name = 'memopolis/your_memes.html'
    
    def get(self, request):
        template=self.template_name
        memes = Meme.objects.filter(author=request.user.id).order_by('-date_posted')

        context = {}
        
        paginator = Paginator(memes, 2)
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

        meme_like_dict = {} 
        for meme in memes:
            meme_like_dict[meme]=meme.num_vote_up
        context['meme_like_dict'] = meme_like_dict
        
        like_sum = 0
        all_memes = Meme.objects.filter(author=request.user.id)
        for meme in all_memes:
            like_sum+=meme.num_vote_up
        context['like_sum']=like_sum
        
        js_meme_title_list = [meme.title for meme in memes]
        context['js_meme_title_list'] = js_meme_title_list
        
        js_meme_like_list = [meme.num_vote_up for meme in memes]
        context['js_meme_like_list'] = js_meme_like_list
        
        return render(request, template, context)
   
def kontakt(request):
    return render(request, 'memopolis/kontakt.html')
