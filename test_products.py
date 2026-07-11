import pytest

def test_product_name(sample_product):
    assert len(sample_product["name"]) > 0

def test_product_category(sample_product):
    assert isinstance(sample_product["category"], str)

@pytest.mark.parametrize("price", [29.99, 9.99, 149.99, 0.01])
def test_price_is_valid(price):
    assert price > 0