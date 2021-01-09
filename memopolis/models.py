from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from vote.models import VoteModel
from users.models import Profile

class Tag(models.Model):
    name = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.name
    
class Meme(VoteModel, models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)

    tags = models.ManyToManyField(Tag, blank=False)

    image = models.ImageField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    
    accepted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('meme-detail', kwargs={'pk':self.pk})
    
    
class Comment(VoteModel, models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    date_posted = models.DateTimeField(default=timezone.now)
    belongs_to = models.ForeignKey(Meme, on_delete=models.CASCADE, null=True, blank=False)
    
    def __str__(self):
        return self.content
    
class Badge(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(null=True)
    parent = models.ManyToManyField(Profile, blank=False)
    date_added_to_parent = models.DateTimeField(default=timezone.now)
    image = models.ImageField(null=True)
    
    def __str__(self):
        return self.title