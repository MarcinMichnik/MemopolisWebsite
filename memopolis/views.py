from django.shortcuts import render
from .models import Meme, Comment
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

class MemeListView(ListView):
    model = Meme
    template_name = 'memopolis/index.html'
    context_object_name = 'memes'
    ordering = ['-date_posted']
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.ordering == ['-date_posted']:
            tops = Meme.objects.order_by('-upvotes')[:3]
            context['tops']=tops
            print('+')
        else:
            print('-')

        return context
    
    def post(self, request):
        
        #receive vote data
        raw = list(request.POST)[1]
        raw = raw.split(' ')
        meme_pk, user_id, vote = raw[0], raw[1], raw[2]

        print(meme_pk, user_id, vote)
        
        #manipulate the values
        #Meme.objects.filter(pk=meme_pk)
        the_meme = Meme.objects.filter(pk=meme_pk)[0]
        
        #list out of the raw text
        list_upvoted_by = the_meme.upvoted_by.split(', ')
        list_downvoted_by = the_meme.downvoted_by.split(', ')
        
        if vote=='up':
            if user_id not in list_upvoted_by and user_id not in list_downvoted_by:
                the_meme.upvotes+=1
                the_meme.upvoted_by+=str(user_id)+', ' 
        elif vote=='down':
            if user_id not in list_downvoted_by and user_id not in list_upvoted_by:
                the_meme.downvotes+=1
                the_meme.downvoted_by+=str(user_id)+', ' 
        print(the_meme.upvoted_by)
        print(the_meme.downvoted_by)
        the_meme.save()
        return HttpResponseRedirect("")
        
class TopMemeListView(MemeListView):
    ordering=["-upvotes"]
    template_name = 'memopolis/top.html'
    
class MemeDetailView(DetailView):
    model = Meme
    
    def post(self, request, *args, **kwargs):

        #receive vote data
        raw = list(request.POST)[1]
        raw = raw.split(' ')
        meme_pk = raw[0]
        user_id = raw[1]
        vote = raw[2]
        print(meme_pk, user_id, vote)

        #manipulate the values
        #Meme.objects.filter(pk=meme_pk)
        the_meme = Meme.objects.filter(pk=meme_pk)[0]

        #list out of the raw text
        list_upvoted_by = the_meme.upvoted_by.split(', ')
        list_downvoted_by = the_meme.downvoted_by.split(', ')

        if vote=='up':
            if user_id not in list_upvoted_by and user_id not in list_downvoted_by:
                the_meme.upvotes+=1
                the_meme.upvoted_by+=str(user_id)+', ' 
        elif vote=='down':
            if user_id not in list_downvoted_by and user_id not in list_upvoted_by:
                the_meme.downvotes+=1
                the_meme.downvoted_by+=str(user_id)+', ' 
        print(the_meme.upvoted_by)
        print(the_meme.downvoted_by)
        the_meme.save()
        return HttpResponseRedirect("")
    
    def make_a_comment(self, request):
        pass
    
class MemeCreateView(CreateView):
    model = Meme
    fields = ['title','tag1','tag2','tag3','image']
    
    def form_valid(self, form):
        form.instance.author = self.request.User
        return super().form_valid(form)
    
def kontakt(request):
    return render(request, "memopolis/kontakt.html")
