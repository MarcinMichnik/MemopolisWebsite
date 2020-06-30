from django.urls import path
from .views import MemeListView, MemeDetailView, MemeCreateView, MemeUpdateView, TopMemeListView, UnacceptedMemeListView, YourMemesListView
from . import views

urlpatterns = [
    path('', MemeListView.as_view(), name="memopolis-index"),
    path('top/', TopMemeListView.as_view(), name="memopolis-top"),
    path('poczekalnia/', UnacceptedMemeListView.as_view(), name="memopolis-unaccepted"),
    path('meme/<int:pk>', MemeDetailView.as_view(), name="meme-detail"),
    path('meme/nowy', MemeCreateView.as_view(), name="meme-create"),
    path('kontakt/', views.kontakt, name="memopolis-kontakt"),
    path('profil/memy', YourMemesListView.as_view(), name="memopolis-your-memes"),
    path('meme/<int:pk>/edytuj/', MemeUpdateView.as_view(), name="meme-edit"),
]
