from django.urls import path

from .views import (ProfileListView, 
                    ProfileDetailView,)

urlpatterns = [
    path('profile/', ProfileListView.as_view()),
    path('profile/<pk>', ProfileDetailView.as_view()),
]