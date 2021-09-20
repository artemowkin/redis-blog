import redis
from django.conf import settings


connection = redis.Redis(**settings.REDIS_DB)
