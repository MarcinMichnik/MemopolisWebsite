from django.shortcuts import render
from .models import Meme
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView

class MemeListView(ListView):
    model = Meme
    template_name = 'memopolis/index.html'
    context_object_name = 'memes'
    ordering = ['-date_posted']
    paginate_by = 2
    
class MemeDetailView(DetailView):
    model = Meme
    
class MemeCreateView(CreateView):
    model = Meme
    fields = ['title','tag1','tag2','tag3','image']
    
    def form_valid(self, form):
        form.instance.author = self.request.User
        return super().form_valid(form)
    
def kontakt(request):
    return render(request, "memopolis/kontakt.html")
