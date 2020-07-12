from django.test import TestCase
from memopolis.models import Tag, Meme, Comment
from django.utils import timezone
from django.contrib.auth.models import User

#models

class TagTest(TestCase):
    def create_tag(self, name="#klaun"):
        return Tag.objects.create(name=name)

    def test_tag_creation(self):
        tag = self.create_tag()
        self.assertTrue(isinstance(tag, Tag))
        self.assertEqual(tag.__str__(), tag.name)
        
class MemeTest(TestCase):
    def create_meme(self, title="Whatever", accepted=False):
        author = User.objects.create()
        return Meme.objects.create(author=author, title=title, accepted=accepted)

    def test_meme_creation(self):
        meme = self.create_meme()
        self.assertTrue(isinstance(meme, Meme))
        self.assertEqual(meme.__str__(), meme.title)
        self.assertEqual(meme.get_absolute_url(), '/meme/1/')
        
class CommentTest(TestCase):
    def create_comment(self, content="A clown is being scary"):
        author = User.objects.create()
        belongs_to = Meme.objects.create(author=author)
        return Comment.objects.create(author=author,content=content)

    def test_comment_creation(self):
        comment = self.create_comment()
        self.assertTrue(isinstance(comment, Comment))
        self.assertEqual(comment.__str__(), comment.content)