from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("users/", views.ListUsersView.as_view(), name="list-users"),
    path("user/<int:pk>/", views.SingleUserView.as_view(), name="single-user"),
    path("images/", views.ListImagesView.as_view(), name="list-images"),
    path("image/<int:pk>/", views.SingleImageView.as_view(), name="single-image"),
    path("albums/", views.ListAlbumsView.as_view(), name="list-albums"),
    path("album/<int:pk>/", views.SingleAlbumView.as_view(), name="single-album"),
    path("album-images/", views.ListAlbumImagesView.as_view(), name="list-album-images"),
    path("album-image/<int:pk>/", views.SingleAlbumImageView.as_view(), name="single-album-image"),
]
