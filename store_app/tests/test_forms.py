import pytest
from store_app.forms import ProductModelForm, CategoryModelForm
from store_app.models import Product, Category


@pytest.mark.django_db
def test_product_form_valid(category):
    form_data = {
        'name': 'Test form',
        'description': 'content form',
        'category': category,
        'price': 30,
    }
    form = ProductModelForm(data=form_data)
    assert form.is_valid()

    cleaned_data = form.cleaned_data
    assert cleaned_data['name'] == form_data['name']


@pytest.mark.django_db
def test_product_model_form_name(category):
    form_data = {
        'name': 'Test',
        'description': 'content form',
        'category': category,
        'price': 30,
    }
    form = ProductModelForm(data=form_data)
    assert not form.is_valid()

@pytest.mark.django_db
def test_product_model_form_description(category):
    form_data = {
        'name': 'Test form',
        'description': 'биба буба',
        'category': category,
        'price': 30,
    }

    form = ProductModelForm(data=form_data)
    assert not form.is_valid()