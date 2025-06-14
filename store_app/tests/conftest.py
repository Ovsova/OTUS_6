import pytest
from store_app.models import Category, Product
from celery import Celery


@pytest.fixture(autouse=True)
def celery_config():
    return {
        'broker_url': 'memory://',
        'result_backend': 'cache+memory://',
    }


@pytest.fixture
def category():
    return Category.objects.create(name='Тестовая категория')


@pytest.fixture
def product(category):
    return Product.objects.create(
        name='Тестовый продукт',
        description='Содержимое текстового поля',
        price=50,
        category=category,
    )


@pytest.fixture
def product2(category):
    return Product.objects.create(
        name='Новый продукт 2',
        description='Содержимое текстового поля 2',
        price=70,
        category=category,
    )
