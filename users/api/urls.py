from django.urls import path

from .views import (ProfileListView, 
                    ProfileDetailView,
                    UserListView, 
                    UserDetailView,)

urlpatterns = [
    path('profile/', ProfileListView.as_view()),
    path('profile/<pk>', ProfileDetailView.as_view()),
    path('user/', UserListView.as_view()),
    path('user/<pk>', UserDetailView.as_view()),
]