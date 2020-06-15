from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
    
class Meme(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    tag1 = models.CharField(max_length=10,null=True)
    tag2 = models.CharField(max_length=10,null=True)
    tag3 = models.CharField(max_length=10,null=True)
    image = models.ImageField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    
    accepted = models.BooleanField(default=False)
    
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    
    upvoted_by = models.TextField(default='n, ')
    downvoted_by = models.TextField(default='n, ')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('meme-detail', kwargs={'pk':self.pk})
    
class Comment(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    date_posted = models.DateTimeField(default=timezone.now)
    belongs_to = models.ForeignKey(Meme, on_delete=models.CASCADE, null=True)
    
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    
    upvoted_by = models.TextField(default='n, ')
    downvoted_by = models.TextField(default='n, ')
    
    def __str__(self):
        return self.content