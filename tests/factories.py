import factory
from django.contrib.auth import get_user_model
from faker import Faker
from books.models import Book, Review


User = get_user_model()
fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: "user_%d" % n)
    email = fake.email()

    class Meta:
        model = User

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = "Testpass54321"
        if "password" in kwargs:
            password = kwargs.pop("password")
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        user.set_password(password)
        if create:
            user.save()
        return user


class BookFactory(factory.django.DjangoModelFactory):
    author = fake.name()
    title = fake.sentence(nb_words=4)
    price = factory.LazyAttribute(
        lambda x: fake.random_number(digits=2) + fake.random_number(digits=2) / 100
    )

    class Meta:
        model = Book


class ReviewFactory(factory.django.DjangoModelFactory):
    author = factory.SubFactory(UserFactory)
    book = factory.SubFactory(BookFactory)
    content = factory.Faker("text", max_nb_chars=254)

    class Meta:
        model = Review
