from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("user.urls")),
    path("", include("photos.urls")),
    path("", include("album.urls")),
    path("api/", include("api.urls")),
]
