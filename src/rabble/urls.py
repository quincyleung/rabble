from django.urls import path
from . import views

urlpatterns = [
    path("", views.subrabble_list, name="index"),
    path("profile", views.profile, name="profile"),
    path("!<slug:name>/", views.subrabble_detail, name="subrabble-detail"),
    path("!<slug:name>/<int:pk>/", views.post_detail, name="post-detail"),
    path("!<slug:name>/new", views.post_create, name="post-create"),
    path("!<slug:name>/<int:pk>/edit", views.post_edit, name="post-edit"),
]