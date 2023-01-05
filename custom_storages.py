from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(s3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(s3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
