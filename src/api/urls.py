from django.urls import path, re_path
from . import views

urlpatterns = [
    path('subrabbles/', views.subrabble_list, name='subrabble_list'),
    path('subrabbles/!<str:identifier>/', views.subrabble_detail, name='subrabble_detail'),
    path('subrabbles/!<str:identifier>/posts/', views.subrabble_post_list, name='subrabble_post_list'),
    path('subrabbles/!<str:identifier>/posts/<int:post_pk>/', views.subrabble_post_detail, name='subrabble_post_detail'),
    path('subrabbles/!<str:identifier>/posts/<int:post_pk>/likes/', views.toggle_like, name='toggle_like'),
]