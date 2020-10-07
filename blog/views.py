from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from blog.models import Author, Post, Comment
from blog.forms import AddCommentForm

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
	pk = request.META.get('HTTP_REFERER')[-1]
	print('\n\n')
	print(pk)
	print('\n\n')
	post = get_object_or_404(Post, pk=pk)

	# POST indicates that this is a submisstion attempt
	if request.method == 'POST':
		form = AddCommentForm(request.POST)

		if form.is_valid():
			# Does any data processing needed by the form
			new_comment = Comment(
				username=request.user.get_username(),
				text=form.cleaned_date['text'],
				post=post,
			)
			new_comment.save()

			return HttpResponseRedirect(reverse(f'posts/{post.id}'))
	# GET indicates that it's a request for a new, empty form
	else:
		form = AddCommentForm()

	context = {
		'form': form,
		'post': post,
	}

	return render(request, 'blog/comment_create.html', context)


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