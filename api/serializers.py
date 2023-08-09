__all__ = [
    "UserSerializer",
    "ImageSerializer",
    "AlbumSerializer",
    "AlbumImageSerializer",
]

from rest_framework import serializers
from user.models import User
from photos.models import Image
from album.models import Album, AlbumImage


class UserSerializer(serializers.ModelSerializer):
    """This is the serializer class for the user model."""

    class Meta:
        model = User

        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "date_joined",
        ]


class ImageSerializer(serializers.ModelSerializer):
    """Serializer class for the image model."""

    user = UserSerializer()
    likes = serializers.SerializerMethodField()

    def get_likes(self, obj) -> int:
        """Get the amount of likes for an image."""
        return obj.likes.count()

    class Meta:
        model = Image

        fields = [
            "id",
            "name",
            "image",
            "status",
            "upload_date",
            "likes",
            "user",
        ]


class AlbumSerializer(serializers.ModelSerializer):
    """Serializer class for the album model."""

    user = UserSerializer()

    class Meta:
        model = Album

        fields = [
            "id",
            "name",
            "status",
            "creation_date",
            "user",
        ]


class AlbumImageSerializer(serializers.ModelSerializer):
    """Serializer for the albumimage model."""

    album = AlbumSerializer()
    user = UserSerializer()

    class Meta:
        model = AlbumImage

        fields = [
            "id",
            "image",
            "upload_date",
            "album",
            "user",
        ]
