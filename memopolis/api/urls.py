from django.urls import path

from .views import (MemeListView, 
                    MemeDetailView, 
                    CommentListView, 
                    CommentDetailView, 
                    TagListView, 
                    TagDetailView)

urlpatterns = [
    path('meme/', MemeListView.as_view()),
    path('meme/<pk>', MemeDetailView.as_view()),
    path('comment/', CommentListView.as_view()),
    path('comment/<pk>', CommentDetailView.as_view()),
    path('tag/', TagListView.as_view()),
    path('tag/<pk>', TagDetailView.as_view()),
]