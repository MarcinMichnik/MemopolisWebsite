from django.contrib import admin
from .models import Meme, Comment, Tag, Badge

admin.site.register(Meme)

admin.site.register(Comment)

admin.site.register(Tag)

admin.site.register(Badge)