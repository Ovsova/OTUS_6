from django.core.management.base import BaseCommand
from store_app.models import Product, Category
from faker import Faker
# import random


class Command(BaseCommand):
    help = 'Generate test data'

    def handle(self, *args, **kwargs):

        self.stdout.write('Start generating test data')
        fake = Faker('ru_RU')
        CATEGORIES = [
            "Электроника",
            "Одежда",
            "Книги",
            "Дом и сад",
            "Спорт",
            "Красота",
            "Игрушки",
            "Продукты"
        ]
        for one_category in CATEGORIES:
            category = Category.objects.create(
            name=one_category,
                description=fake.sentence()
            )
            for _ in range(5):
                Product.objects.create(
                    name=fake.word().capitalize(),
                    description=fake.paragraph(nb_sentences=3),
                    price=fake.random_int(min=100, max=1000),
                    category=category,
                    created_at=fake.date_this_year()
                )
            self.stdout.write('Категория создана')

        self.stdout.write('Stop generating test data')