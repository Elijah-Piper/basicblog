from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('posts/', views.PostListView.as_view(), name='post-list'),
	path('posts/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
	path('authors/', views.AuthorListView.as_view(), name='author-list'),
	path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
	path('addcomment/', views.add_comment_view, name='comment-create'),
	path('addpost/', views.add_post_view, name='post-create'),
]