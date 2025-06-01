import pytest
from store_app.models import Product, Category
from django.urls import reverse
from django.contrib.messages import get_messages

@pytest.mark.django_db
def test_category_creation(category):
    assert Category.objects.count() == 1
    assert category.name == 'Тестовая категория'
    assert str(category) == 'Тестовая категория'

@pytest.mark.django_db
def test_product_creation(product):
    assert Product.objects.count() == 1
    assert product.name == 'Тестовый продукт'
    assert product.category.name == 'Тестовая категория'


@pytest.mark.django_db
def test_product_update_view(client, product):
    url = reverse('edit_product', kwargs={'pk': product.pk})
    response = client.get(url)
    assert response.status_code == 200

    data = {
        'name': 'Обновленный продукт',
        'description': 'Новое описание',
        'price': 150,
        'category': product.category.pk
    }
    response = client.post(url, data)
    assert response.status_code == 302
    product.refresh_from_db()
    assert product.name == 'Обновленный продукт'

    messages = list(get_messages(response.wsgi_request))
    assert str(messages[0]) == 'Продукт успешно обновлен'


@pytest.mark.django_db
def test_product_delete_view(client, product):
    url = reverse('delete_product', kwargs={'pk': product.pk})
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url)
    assert response.status_code == 302
    assert not Product.objects.filter(pk=product.pk).exists()