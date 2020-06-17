from django.shortcuts import render
from .models import Meme, Comment
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

class MemeListView(ListView):
    model = Meme
    template_name = 'memopolis/index.html'
    
    def get_context_data(self, **kwargs):
        context = {}

        if self.template_name == 'memopolis/index.html':
            tops = Meme.objects.order_by('-upvotes')[:3]
            context['tops']=tops
            
            # only accepted memes
            memes = Meme.objects.order_by('-date_posted').filter(accepted=True)
            context['memes']=memes
            
        else:
            context = super().get_context_data(**kwargs)

        return context
    
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
                the_meme.downvoted_by+=' '+str(user_id)+','
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
        print(context)
        meme = context['meme']
        comments = Comment.objects.filter(belongs_to=meme)
        context['comments'] = comments

        return context
    
    
    def post(self, request, *args, **kwargs):
        
        #receive vote data
        raw = list(request.POST)[1]
        raw = raw.split(' ')
        object_pk = raw[0]
        user_id = raw[1]
        vote = raw[2]
        direction = raw[3]
        
        if direction == 'meme':
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
                    the_meme.upvoted_by+=' '+str(user_id)+','
            elif vote=='down':
                if user_id not in list_downvoted_by and user_id not in list_upvoted_by:
                    the_meme.downvotes+=1
                    the_meme.downvoted_by+=' '+str(user_id)+','
            the_meme.save()
            
        elif direction == 'comment':
            print(object_pk, user_id, vote)

            #manipulate the values
            #Meme.objects.filter(pk=object_pk)
            the_comment = Comment.objects.filter(pk=object_pk)[0]

            #list out of the raw text
            list_upvoted_by = the_comment.upvoted_by.split(', ')
            list_downvoted_by = the_comment.downvoted_by.split(', ')

            if vote=='up':
                if user_id not in list_upvoted_by and user_id not in list_downvoted_by:
                    the_comment.upvotes+=1
                    the_comment.upvoted_by+=' '+str(user_id)+','
            elif vote=='down':
                if user_id not in list_downvoted_by and user_id not in list_upvoted_by:
                    the_comment.downvotes+=1
                    the_comment.downvoted_by+=' '+str(user_id)+','
            the_comment.save()
            
        return HttpResponseRedirect("")
    
class MemeCreateView(CreateView):
    model = Meme
    fields = ['title','tag1','tag2','tag3','image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

    
def kontakt(request):
    return render(request, "memopolis/kontakt.html")
