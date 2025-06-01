import pytest
from django.urls import reverse
from store_app.models import Product, Category

def test_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Главная страница Магазина.' in response.content.decode('utf-8')

@pytest.mark.django_db
def test_post_list(client, category, product):
    url = reverse('products')
    response = client.get(url)
    assert response.status_code == 200
    assert product.name.encode() in response.content
    assert category.name.encode() in response.content

@pytest.mark.django_db
def test_post_filter(client, category, product):
    url = reverse('products')
    response = client.get(url, {'rating': 7})
    assert product.name in response.content.decode('utf-8')

    low_coast_post = Product.objects.create(
        name= 'Низкий рейтинг',
        description='Тут низкий рейтинг',
        price=2,
        category=category,
    )
    assert low_coast_post.name not in response.content.decode('utf-8')