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
        
        
                
        return HttpResponseRedirect("")
class MemeCreateView(CreateView):
    model = Meme
    fields = ['title','image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

    
def kontakt(request):
    return render(request, "memopolis/kontakt.html")
