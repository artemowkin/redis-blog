from django.urls import path

from . import views


urlpatterns = [
	path('', views.AllPosts.as_view(), name='all_posts'),
	path(
		'<uuid:post_id>/like/', views.AddPostLike.as_view(),
		name='add_post_like'),
	path(
		'<uuid:post_id>/unlike/', views.UnlikePost.as_view(),
		name='unlike_post'),
]
