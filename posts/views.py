from django.core.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.response import Response

from . import services
from .serializers import PostSerializer


class AllPosts(APIView):
	serializer_class = PostSerializer

	def get(self, request):
		all_posts = services.get_all_posts()
		serialized_posts = self.serializer_class(all_posts, many=True).data
		return Response(serialized_posts)

	def post(self, request):
		if not request.user.is_authenticated:
			raise PermissionDenied

		created_post = services.create_post(
			title=request.data['title'],
			text=request.data['text'], author=request.user
		)
		serialized_post = self.serializer_class(created_post).data
		return Response(serialized_post, status=201)


class AddPostLike(APIView):

	def post(self, request, post_id):
		if not request.user.is_authenticated:
			raise PermissionDenied

		post = services.get_concrete_post(post_id)
		if services.check_user_liked_post(post, request.user):
			return Response({
				"errors": ["You are already liked this post"]
			}, status=400)

		services.add_post_like(post, request.user)
		return Response(status=204)


class UnlikePost(APIView):

	def post(self, request, post_id):
		if not request.user.is_authenticated:
			raise PermissionDenied

		post = services.get_concrete_post(post_id)
		if not services.check_user_liked_post(post, request.user):
			return Response({
				"errors": ["You were not liked this post"]
			}, status=400)

		services.unlike_post(post, request.user)
		return Response(status=204)
