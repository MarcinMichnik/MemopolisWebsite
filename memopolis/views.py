from django.shortcuts import render
from .models import Meme, Comment
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView
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
            tops = Meme.objects.order_by('-upvotes')[:3]
            context['tops']=tops

        return context
    
    def get(self, request):
        context = self.get_context_data()
        template = self.template_name
        
        if self.template_name == 'memopolis/index.html':
            meme_list = Meme.objects.order_by('-date_posted').filter(accepted=True)
        elif self.template_name == 'memopolis/top.html':
            meme_list = Meme.objects.order_by('-upvotes').filter(accepted=True)
        elif self.template_name == 'memopolis/unaccepted_memes.html':
            meme_list = Meme.objects.order_by("-date_posted").filter(accepted=False)
            
        paginator = Paginator(meme_list, 2)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj

        return render(request, template, context)

    def post(self, request):
        
        #receive vote data
        raw = list(request.POST)[1]
        raw = raw.split(' ')
        object_pk, user_id, vote = raw[0], raw[1], raw[2]

        print(object_pk, user_id, vote)
        
        #manipulate the values
        #Meme.objects.filter(pk=object_pk)
        the_meme = Meme.objects.filter(pk=object_pk)[0]
        
        #list out of the raw text
        list_upvoted_by = the_meme.upvoted_by.split(', ')
        list_downvoted_by = the_meme.downvoted_by.split(', ')
        
        if vote=='up':
            if user_id not in list_upvoted_by and user_id not in list_downvoted_by:
                the_meme.upvotes+=1
                the_meme.upvoted_by+=' '+str(user_id)+','+' '+','
        elif vote=='down':
            if user_id not in list_downvoted_by and user_id not in list_upvoted_by:
                the_meme.downvotes+=1
                the_meme.downvoted_by+=' '+str(user_id)+','+' '+','
        the_meme.save()
        return HttpResponseRedirect("")
        
class TopMemeListView(MemeListView):
    template_name = 'memopolis/top.html'
    
    def get_context_data(self, **kwargs):
        context = {}
        if self.template_name == 'memopolis/top.html':
            memes = Meme.objects.order_by('-upvotes').filter(accepted=True)
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
        
        #receive vote data
        raw = list(request.POST)[1]
        raw = raw.split(' ')
        direction = 0
        if len(raw)>1:
            object_pk = raw[0]
            user_id = raw[1]
            vote = raw[2]
            direction = raw[3]
        
        if direction == 'meme':

            #manipulate the values
            #Meme.objects.filter(pk=object_pk)
            the_meme = Meme.objects.filter(pk=object_pk)[0]

            #list out of the raw text
            list_upvoted_by = the_meme.upvoted_by.split(', ')
            list_downvoted_by = the_meme.downvoted_by.split(', ')

            if vote=='up':
                if user_id not in list_upvoted_by and user_id not in list_downvoted_by:
                    the_meme.upvotes+=1
                    the_meme.upvoted_by+=' '+str(user_id)+','+' '+','
            elif vote=='down':
                if user_id not in list_downvoted_by and user_id not in list_upvoted_by:
                    the_meme.downvotes+=1
                    the_meme.downvoted_by+=' '+str(user_id)+','+' '+','
            the_meme.save()
            
        elif direction == 'comment':

            #manipulate the values
            #Meme.objects.filter(pk=object_pk)
            the_comment = Comment.objects.filter(pk=object_pk)[0]

            #list out of the raw text
            list_upvoted_by = the_comment.upvoted_by.split(', ')
            list_downvoted_by = the_comment.downvoted_by.split(', ')

            if vote=='up':
                if user_id not in list_upvoted_by and user_id not in list_downvoted_by:
                    the_comment.upvotes+=1
                    the_comment.upvoted_by+=' '+str(user_id)+','+' '+','
            elif vote=='down':
                if user_id not in list_downvoted_by and user_id not in list_upvoted_by:
                    the_comment.downvotes+=1
                    the_comment.downvoted_by+=' '+str(user_id)+','+' '+','
            the_comment.save()
            
        else:
            self.object = self.get_object()
            form = CommentRegisterForm(data=request.POST)
            
            if form.is_valid():
                new_comment = Comment()

                new_comment.author_id = request.user
                

                form.is_valid()
                content = form.cleaned_data['content']            
                new_comment.content = content

                new_comment.belongs_to = self.object

                new_comment.save()
                
        return HttpResponseRedirect("")
class MemeCreateView(CreateView):
    model = Meme
    fields = ['title','tag1','tag2','tag3','image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

    
def kontakt(request):
    return render(request, "memopolis/kontakt.html")
