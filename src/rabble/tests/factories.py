import string

import factory
from factory import Sequence, Faker, SubFactory
from factory.django import DjangoModelFactory
from rabble.models import User, Community, SubRabble, Post, Comment

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
    
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('email')
    username = factory.LazyAttribute(lambda obj: f"{obj.first_name.lower()}.{obj.last_name.lower()}")
    bio = Faker('text', max_nb_chars=150)
    interests = Faker('sentence', nb_words=4)
    avatar_url = Faker('image_url')

class CommunityFactory(DjangoModelFactory):
    class Meta:
        model = Community
        skip_postgeneration_save = True

    name = Faker('word')
    owner = SubFactory(UserFactory)
    
    @factory.post_generation
    def admins(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for user in extracted:
                self.admins.add(user)
        else:
            self.admins.add(UserFactory(), UserFactory())

class SubRabbleFactory(DjangoModelFactory):
    class Meta:
        model = SubRabble

    name = Sequence(lambda n: f"subrabble-{n}")
    display_name = factory.LazyAttribute(lambda obj: obj.name.title())
    description = Faker('text', max_nb_chars=150)
    community = SubFactory(CommunityFactory)
    public = Faker('boolean')
    allow_anonymous = Faker('boolean')

class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = Faker('sentence', nb_words=5)
    body = Faker('text')
    subrabble = SubFactory(SubRabbleFactory)
    user = SubFactory(UserFactory)
    created_at = Faker('date_time_this_year')
    anonymous = Faker('boolean')

class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    body = Faker('text')
    post = SubFactory(PostFactory)
    user = SubFactory(UserFactory)
    created_at = Faker('date_time_this_year')