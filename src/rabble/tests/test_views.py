import pytest
from django.urls import reverse
from django.core.management import call_command
from rabble.models import User, Community, SubRabble, Post, Comment
from .factories import UserFactory, CommunityFactory, SubRabbleFactory, PostFactory, CommentFactory

@pytest.fixture
def logged_in_client(client):
    user = UserFactory()
    client.force_login(user)
    return client

@pytest.mark.django_db
def test_index_view(logged_in_client):
    # Create the "default" community and subrabbles
    default_community = CommunityFactory.create(name="default")
    subrabbles = SubRabbleFactory.create_batch(5, community=default_community)
    response = logged_in_client.get(reverse('index'))
    assert response.status_code == 200

    html = response.content.decode()
    for subrabble in subrabbles:
        assert subrabble.name in html
        assert subrabble.description in html
        assert subrabble.display_name in html

@pytest.mark.django_db
def test_subrabble_detail_view(logged_in_client):
    subrabble = SubRabbleFactory.create()
    # Create some posts and comments
    posts = PostFactory.create_batch(5, subrabble=subrabble)
    for post in posts:
        CommentFactory.create_batch(2, post=post)
    response = logged_in_client.get(reverse('subrabble-detail', args=[subrabble.name]))

    assert response.context['subrabble'] == subrabble
    assert response.status_code == 200

    html = response.content.decode()
    assert str(subrabble.posts.count()) in html
    assert html.count('<span class="badge bg-secondary">2</span>') == 5

@pytest.mark.django_db
def test_post_create_view(logged_in_client):
    # Create a subrabble and post
    subrabble = SubRabbleFactory.create()
    data = {
        'title': 'Test Post',
        'body': 'This is a test post :)',
        'subrabble': subrabble.pk,
        'anonymous': False
    }
    response = logged_in_client.post(reverse('post-create', args=[subrabble.name]), data=data)
    assert response.status_code == 302

    assert Post.objects.count() == 1
    assert Post.objects.first().title == data['title']
    assert Post.objects.first().body == data['body']
    assert Post.objects.first().subrabble == subrabble


