from django.db import models
from user.models import User


class Image(models.Model):
    """This model holds information for user uploaded images"""

    # Status of the image
    class Status(models.TextChoices):
        PUBLIC = 'public', 'Public'
        PRIVATE = 'private', 'Private'

    name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(upload_to='images/')
    status = models.CharField(
        max_length=7, choices=Status.choices, default=Status.PUBLIC)
    upload_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='photos')

    def __str__(self) -> str:
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='name_idx'),
            models.Index(fields=['user'], name='user_idx')
        ]

        ordering = ['-upload_date']