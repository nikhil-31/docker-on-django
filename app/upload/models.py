from django.db import models
from hellodjango.storage_backends import PublicMediaStorage, PrivateMediaStorage


# Create your models here.
class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=PublicMediaStorage())


class PrivateUpload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=PrivateMediaStorage())
