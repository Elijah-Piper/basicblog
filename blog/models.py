from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Author(models.Model):
	"""Model for representing individual blog authors."""
	account_username = models.CharField(
		max_length=50,
		help_text="The user permissioned user account associated with this author"
	)
	
	name = models.CharField(
		max_length=50,
		help_text="The name displayed for this author"
	)

	bio = models.CharField(
		max_length=1000,
		help_text="The biographical information for this blogger"
	)

	def __str__(self):
		return f'{self.name} - {self.account_username}'

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

	class Meta:
		ordering = ['name', 'account_username']


class Post(models.Model):
	"""Model for an individual blog post."""
	# One to many-to-many relationship; one author to many blog posts
	author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)

	title = models.CharField(
		max_length=60,
		help_text="The title to display for this blog post"
	)

	# The date published
	posted = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False)

	# The text body of the blog post
	text = models.TextField(
		help_text="The body of the blog post"
	)

	def __str__(self):
		return f'{self.title} - by {self.author}'

	def get_absolute_url(self):
		return reverse('post-detail', args=[str(self.id)])

	class Meta:
		ordering = ['-posted']
		permissions = (("can_post", "Can author blog posts"),)


class Comment(models.Model):
	"""Model for an individual comment on a blog post."""
	username = models.CharField(
		max_length=50,
		help_text="The user who authored this blog post"
	)

	# The date published
	posted = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False)

	# The text body of the comment to be displayed
	text = models.TextField(
		max_length=500,
		help_text="The text to display in the comment"
	)

	# One-to-many relationship; 'Post' model as a string because it hasn't been
	# 	declared in a file yet.
	post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return f'Comment {self.posted} - {self.username} - {self.post}'

	class Meta:
		ordering = ['posted']