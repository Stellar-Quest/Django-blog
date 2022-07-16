import datetime
from unittest import TestCase

from django.utils import timezone

from .models import Post


class PostModelTest(TestCase):
    def test_old_post_was_published_recently(self):
        time = timezone.now() - datetime.timedelta(days=30)
        post = Post(
            title='Old_post',
            text='Some text for test',
            published=time,
        )
        self.assertFalse(post.was_published_recently())

    def test_recent_post_was_published_recently(self):
        time = timezone.now() - datetime.timedelta(hours=4)
        post = Post(
            title='Recent_post',
            text='Some text for test',
            published=time,
        )
        self.assertTrue(post.was_published_recently())
