from django.shortcuts import render
from .models import Meme
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

class MemeListView(ListView):
    model = Meme
    template_name = 'memopolis/index.html'
    context_object_name = 'memes'
    ordering = ['-date_posted']
    paginate_by = 2
    
class MemeDetailView(DetailView):
    model = Meme
    
def kontakt(request):
    return render(request, "memopolis/kontakt.html")
