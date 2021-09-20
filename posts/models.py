from uuid import uuid4

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
	uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
	title = models.CharField(max_length=255)
	text = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	pub_date = models.DateField(auto_now_add=True)

	class Meta:
		db_table = 'posts'
		ordering = ('pub_date', 'title')

	@property
	def likes(self):
		from .services import get_post_likes
		return get_post_likes(self)
