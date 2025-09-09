from app import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_homepage(client):
    response = client.get("/")
    print(response)
    print(response.get_json())
    assert response.status_code == 200
    assert "welcome" in response.get_json()["message"].lower()

def test_get_all_products(client):
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
    assert len(response.get_json()) >= 3

def test_get_product_by_id(client):
    response = client.get("/products/2")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Book"

def test_get_product_by_invalid_id(client):
    response = client.get("/products/99")
    assert response.status_code == 404

def test_get_products_by_category(client):
    response = client.get("/products?category=books")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert all(p["category"].lower() == "books" for p in data)
