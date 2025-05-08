import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rabble.models import User, Community, SubRabble, Post, Comment
from .factories import UserFactory, CommunityFactory, SubRabbleFactory, PostFactory, CommentFactory

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_subrabble_get(api_client):
    subrabble = SubRabbleFactory.create()
    response = api_client.get(reverse('subrabble_detail', args=[subrabble.name]))
    
    # Check the response
    assert response.status_code == 200
    assert response.data['name'] == subrabble.name
    assert response.data['display_name'] == subrabble.display_name
    assert response.data['description'] == subrabble.description
    assert response.data['community'] == subrabble.community.pk
    assert response.data['public'] == subrabble.public
    assert response.data['allow_anonymous'] == subrabble.allow_anonymous

@pytest.mark.django_db
def test_post_post(api_client):
    subrabble = SubRabbleFactory.create()
    user = UserFactory.create()

    data = {
        'title': 'Test Post',
        'body': 'This is a test post :)',
        'subrabble': subrabble.pk,
        'username': user.username,
        'anonymous': False
    }
    response = api_client.post(reverse('subrabble_post_list', args=[subrabble.name]), data)
    assert response.status_code == 201

    # Confirm the object was created
    assert Post.objects.count() == 1
    assert Post.objects.first().title == data['title']
    assert Post.objects.first().body == data['body']
    assert Post.objects.first().subrabble == subrabble

    print(response.status_code)
    print(response.json()) 

@pytest.mark.django_db
def test_post_patch(api_client):
    post = PostFactory.create()
    data = {
        'title': 'Updated Title',
        'body': 'Updated body text.'
    }
    response = api_client.patch(reverse('subrabble_post_detail', args=[post.subrabble.name, post.pk]), data)
    assert response.status_code == 200

    # Verify the post was updated on the database
    post.refresh_from_db()
    assert post.title == data['title']
    assert post.body == data['body']