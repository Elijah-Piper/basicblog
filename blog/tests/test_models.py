from django.test import TestCase

from blog.models import Author, Post, Comment 

class AuthorModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		"""Runs once for entire class."""
		# Creates a test author
		test_author = Author(
			account_username="testusername",
			name="John Doe",
			bio="I am anonymous."
		)
		test_author.save()

	def test_get_absolute_url(self):
		author = Author.objects.get(id=1)
		abs_url = author.get_absolute_url()
		self.assertEqual(abs_url, '/blog/authors/1')

	def test_bio_max_length(self):
		author = Author.objects.get(id=1)
		max_length = author._meta.get_field('bio').max_length
		self.assertEqual(max_length, 1000)


class PostModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		"""Runs once for entire class."""
		# Creates a test author
		test_author = Author(
			account_username="testusername",
			name="John Doe",
			bio="I am anonymous."
		)
		test_author.save()

		# Creates a test post
		test_post = Post(
			author=test_author,
			title='Test Blog Post Title',
			text='This sentence is the blog body.'
		)
		test_post.save()

	def test_get_absolute_url(self):
		post = Post.objects.get(id=1)
		abs_url = post.get_absolute_url()
		self.assertEqual(abs_url, '/blog/posts/1')

	def test_title_max_length(self):
		post = Post.objects.get(id=1)
		max_length = post._meta.get_field('title').max_length
		self.assertEqual(max_length, 60)


class CommentModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		"""Runs once for entire class."""
		# Creates a test author
		test_author = Author(
			account_username="testusername_author",
			name="John Doe",
			bio="I am anonymous."
		)
		test_author.save()

		# Creates a test post
		test_post = Post(
			author=test_author,
			title='Test Blog Post Title',
			text='This sentence is the blog body.'
		)
		test_post.save()

		# Creates a test comment
		test_comment = Comment(
			username='testusername_commenter',
			text='comment...comment...comment...comment',
			post=test_post
		)
		test_comment.save()

	def test_comment_text_max_length(self):
		comment = Comment.objects.get(id=1)
		max_length = comment._meta.get_field('text').max_length
		self.assertEqual(max_length, 500)