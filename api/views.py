from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from user.models import User
from photos.models import Image, ImageLikes
from album.models import Album, AlbumImage
from . import serializers


class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class SingleUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ListImagesView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer


class SingleImageView(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer


class ListAlbumsView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer


class SingleAlbumView(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer
    permission_classes = [IsAuthenticated]


class ListAlbumImagesView(generics.ListAPIView):
    queryset = AlbumImage.objects.all()
    serializer_class = serializers.AlbumImageSerializer


class SingleAlbumImageView(generics.RetrieveAPIView):
    queryset = AlbumImage.objects.all()
    serializer_class = serializers.AlbumImageSerializer
