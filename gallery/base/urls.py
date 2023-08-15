from django.urls import path

from . import views
from .views import PhotoDeleteView


urlpatterns = [
    path("", views.index, name="index"),
    path("create_album", views.create_album, name="create_album"),
    path("album/<pk>/", views.album, name="album"),
    path("upload", views.upload, name="upload"),
    path("<pk>/delete/", PhotoDeleteView.as_view()),
    path("map/<pk>/", views.map_photos, name="map"),
]
