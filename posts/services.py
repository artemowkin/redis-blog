from django.shortcuts import get_object_or_404

from redisblog.redis_db import connection
from .models import Post


def get_all_posts():
	all_posts = Post.objects.all()
	return all_posts


def get_concrete_post(post_id):
	post = get_object_or_404(Post, uuid=post_id)
	return post


def create_post(title, text, author):
	post = Post.objects.create(title=title, text=text, author=author)
	return post


def get_post_likes(post):
	if connection.exists(f"post:{post.uuid}"):
		return connection.scard(f"post:{post.uuid}")

	return 0


def add_post_like(post, user):
	return connection.sadd(f"post:{post.uuid}", str(user.id))


def check_user_liked_post(post, user):
	if connection.exists(f"post:{post.uuid}"):
		return connection.sismember(f"post:{post.uuid}", str(user.id))

	return False


def unlike_post(post, user):
	connection.srem(f"post:{post.uuid}", str(user.id))
