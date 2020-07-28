from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView)
from memopolis.models import Meme, Comment, Tag
from .serializers import MemeSerializer, CommentSerializer, TagSerializer

class MemeListView(ListAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
    
class MemeDetailView(RetrieveAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
    
    
class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class CommentDetailView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    
class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
class TagDetailView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer