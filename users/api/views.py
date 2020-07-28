from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView)
from users.models import Profile
from .serializers import ProfileSerializer

class ProfileListView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class ProfileDetailView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer