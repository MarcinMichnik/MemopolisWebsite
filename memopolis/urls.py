from django.urls import path
from .views import MemeListView, MemeDetailView
from . import views

urlpatterns = [
    path('', MemeListView.as_view(), name="memopolis-index"),
    path('meme/<int:pk>', MemeDetailView.as_view(), name="meme-detail"),
    path('kontakt/', views.kontakt, name="memopolis-kontakt"),
]
