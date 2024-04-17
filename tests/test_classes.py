import pytest
from src.classes import Category, Product

@pytest.fixture
def sample_product():
    return [Product("Мышь APPLE Magic Mouse", "Apple Magic Mouse 3 — многофункциональная мышь", 9128, 100),
            Product("Смартфон Apple iPhone 15 256 ГБ", "Встречайте iPhone 15", 90366, 50)]


@pytest.fixture
def sample_category(sample_product):
    return Category("Электроника", "Электроника компании Apple", sample_product)

def test_category_initialization(sample_category, sample_product):
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Электроника компании Apple"
    assert sample_category.goods == ['Мышь APPLE Magic Mouse, 9128 руб. Остаток: 100 шт.', 'Смартфон Apple iPhone 15 256 ГБ, 90366 руб. Остаток: 50 шт.']
    assert sample_product[0].name == "Мышь APPLE Magic Mouse"
    assert sample_product[0].description == "Apple Magic Mouse 3 — многофункциональная мышь"
    assert sample_product[0].price == 9128
    assert sample_product[0].quantity == 100

def test_product(sample_category, sample_product):
    assert Category.unique_products == 2
    assert Category.total_number == 4

