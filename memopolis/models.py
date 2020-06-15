from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    date_posted = models.DateTimeField(default=timezone.now)
    
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    
    upvoted_by = models.TextField(null=True)
    downvoted_by = models.TextField(null=True)
    
    def __str__(self):
        return self.author
    
class Meme(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    tag1 = models.CharField(max_length=10,null=True)
    tag2 = models.CharField(max_length=10,null=True)
    tag3 = models.CharField(max_length=10,null=True)
    image = models.ImageField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    
    upvoted_by = models.TextField(null=True)
    downvoted_by = models.TextField(null=True)
    
    def __str__(self):
        return self.title

    def comment(self, comment_obj):
        self.comments.append(comment_obj)