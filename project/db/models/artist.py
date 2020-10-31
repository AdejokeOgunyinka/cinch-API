import uuid
from django.db import models
from django.contrib.auth import get_user_model


class Artist(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id     = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    firstname   = models.CharField(max_length=30, null=True)
    lastname    = models.CharField(max_length=30, null=True)
    avatar_url  = models.CharField(max_length=255, null=True)
    created_at  = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f" {self.firstname} {self.lastname}"
