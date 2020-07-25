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
    def create_meme(self, title="Test Title", accepted=False):
        author = User.objects.create()
        return Meme.objects.create(author=author, title=title, accepted=accepted)

    def test_meme_creation(self):
        meme = self.create_meme()
        self.assertTrue(isinstance(meme, Meme))
        self.assertEqual(meme.__str__(), meme.title)
        self.assertEqual(meme.get_absolute_url(), '/meme/1/')
        
class CommentTest(TestCase):
    def create_comment(self, content="This is a test."):
        author = User.objects.create()
        belongs_to = Meme.objects.create(author=author)
        return Comment.objects.create(author=author,content=content)

    def test_comment_creation(self):
        comment = self.create_comment()
        self.assertTrue(isinstance(comment, Comment))
        self.assertEqual(comment.__str__(), comment.content)


# views (uses reverse)

def test_memopolis_list_view(self):
    view = self.create_whatever()
    url = reverse("whatever.views.whatever")
    resp = self.client.get(url)

    self.assertEqual(resp.status_code, 200)
    self.assertIn(w.title, resp.content)
    
# views (uses selenium)

import unittest
from selenium import webdriver
class TestDataChange(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_data_change_fire(self):
        self.driver.get("http://localhost:8000/profil")
        self.driver.find_element_by_id('id_username').send_keys("test name")
        self.driver.find_element_by_id('id_email').send_keys("test@ls.fl")
        self.driver.find_element_by_type('submit').click()
        self.assertIn("http://localhost:8000/profil", self.driver.current_url)

    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()