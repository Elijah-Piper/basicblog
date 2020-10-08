from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from blog.models import Author, Post, Comment
from blog.forms import AddCommentForm, AddPostForm

def index(request):
	"""
	Basic view function for the index/site home page.
	Takes a request and returns an HttpResponse.
	"""

	context = {
	
	}

	return render(request, 'index.html', context=context)

def add_comment_view(request):
	"""View for adding a comment to a particular post."""
	# POST indicates that this is a submisstion attempt
	if request.method == 'POST':
		form = AddCommentForm(request.POST)

		if form.is_valid():
			# Does any data processing needed by the form
			post = Post.objects.get(id__exact=form.cleaned_data['post_id'])
			new_comment = Comment(
				username=request.user.get_username(),
				text=form.cleaned_data['text'],
				post=post,
			)
			new_comment.save()

			return HttpResponseRedirect(reverse(f'post-list'))
	# GET indicates that it's a request for a new, empty form
	else:
		form = AddCommentForm()

	context = {
		'form': form,
	}

	return render(request, 'blog/comment_create.html', context)

@permission_required('blog.can_post')
def add_post_view(request):
	"""View for the post creation form."""
	# Finds the author model record for the associated user
	user = request.user.get_username()
	for author in Author.objects.all():
		if author.account_username == user:
			current_author = author
			break

	# POST indicates that it is an attempt to submit data
	if request.method == "POST":
		form = AddPostForm(request.POST)

		if form.is_valid():
			# Does data processing for creating a new post
			new_post = Post(
				author=current_author,
				title=form.cleaned_data['title'],
				text=form.cleaned_data['text'],
			)
			new_post.save()

			return HttpResponseRedirect(reverse('post-list'))
	# Get indicates a request for a fresh form for writing a new post
	else:
		form = AddPostForm()

		context = {
			'form': form,
		}

		return render(request, 'blog/create_post.html', context)

class PostListView(generic.ListView):
	"""View for the list of all blog posts."""
	model = Post
	paginate_by = 5


class PostDetailView(generic.DetailView):
	"""View for displaying the detail page for individual blog posts."""
	model = Post


class AuthorListView(generic.ListView):
	"""Generic class-based list view for displaying a list of author links."""
	model = Author


class AuthorDetailView(generic.DetailView):
	"""Generic class-based detail view for individual author information."""
	model = Author