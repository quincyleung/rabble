import pytest
from rabble.models import User, Community, SubRabble, Post, Comment 
from .factories import UserFactory, CommunityFactory, SubRabbleFactory, PostFactory, CommentFactory

@pytest.mark.django_db
def test_create_user():
    # Create a single user instance using the factory
    user = UserFactory.create()

    # Verify the user count in the database
    assert User.objects.count() == 1

    # Fetch the user from the database
    db_user = User.objects.get(username=user.username)

    # Verify the user's attributes
    assert db_user.first_name == user.first_name
    assert db_user.last_name == user.last_name
    assert db_user.email == user.email
    assert db_user.username == user.username
    assert db_user.bio == user.bio
    assert db_user.interests == user.interests
    assert db_user.avatar_url == user.avatar_url

@pytest.mark.django_db
def test_create_community():
    # Create a single community instance using the factory
    community = CommunityFactory.create()

    # Verify the community count in the database
    assert Community.objects.count() == 1

    # Fetch the community from the database
    db_community = Community.objects.get(name=community.name)

    # Verify the community's attributes
    assert db_community.name == community.name
    assert db_community.owner == community.owner
    assert db_community.admins.count() == 2
    assert all(admin in db_community.admins.all() for admin in community.admins.all())

@pytest.mark.django_db
def test_create_subrabble():
    # Create a single subrabble instance using the factory
    subrabble = SubRabbleFactory.create()

    # Verify the subrabble count in the database
    assert SubRabble.objects.count() == 1

    # Fetch the subrabble from the database
    db_subrabble = SubRabble.objects.get(name=subrabble.name)

    # Verify the subrabble's attributes
    assert db_subrabble.name == subrabble.name
    assert db_subrabble.display_name == subrabble.display_name
    assert db_subrabble.description == subrabble.description
    assert db_subrabble.community == subrabble.community
    assert db_subrabble.public == subrabble.public
    assert db_subrabble.allow_anonymous == subrabble.allow_anonymous

@pytest.mark.django_db
def test_create_post():
    # Create a single post instance using the factory
    post = PostFactory.create()

    # Verify the post count in the database
    assert Post.objects.count() == 1

    # Fetch the post from the database
    db_post = Post.objects.get(title=post.title)

    # Verify the post's attributes
    assert db_post.title == post.title
    assert db_post.body == post.body
    assert db_post.subrabble == post.subrabble
    assert db_post.user == post.user
    assert db_post.created_at == post.created_at
    assert db_post.anonymous == post.anonymous

@pytest.mark.django_db
def test_create_multiple_posts():
    PostFactory.create_batch(5)
    assert Post.objects.count() == 5

@pytest.mark.django_db
def test_create_comment():
    # Create a single comment instance using the factory
    comment = CommentFactory.create()

    # Verify the comment count in the database
    assert Comment.objects.count() == 1

    # Fetch the comment from the database
    db_comment = Comment.objects.get(body=comment.body)

    # Verify the comment's attributes
    assert db_comment.body == comment.body
    assert db_comment.post == comment.post
    assert db_comment.user == comment.user
    assert db_comment.created_at == comment.created_at
