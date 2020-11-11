from rest_framework import serializers
from memopolis.models import Meme, Comment, Tag

class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = ['id', 'author', 'title', 'num_vote_up', 'tags', 'image', 'date_posted', 'accepted']
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'num_vote_up', 'date_posted', 'belongs_to']
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']