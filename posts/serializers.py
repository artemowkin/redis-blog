from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
	likes = serializers.IntegerField(min_value=0, default=0, read_only=True)

	class Meta:
		model = Post
		fields = ('pk', 'title', 'text', 'author', 'pub_date', 'likes')
		read_only_fields = ('pk', 'author', 'pub_date', 'likes')
