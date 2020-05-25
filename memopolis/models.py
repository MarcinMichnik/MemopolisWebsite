from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Meme(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    tag1 = models.CharField(max_length=10,null=True)
    tag2 = models.CharField(max_length=10,null=True)
    tag3 = models.CharField(max_length=10,null=True)
    image = models.ImageField(blank=True, null=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
