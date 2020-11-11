from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView)
from users.models import Profile
from .serializers import ProfileSerializer
from users.models import User
from .serializers import UserSerializer

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileListView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class ProfileDetailView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer