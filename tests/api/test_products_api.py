import requests

def test_products_api():
    response = requests.get("https://automationexercise.com/api/productsList")
    assert response.status_code == 200
    data = response.json()
    assert 'products' in data
    assert data['products']
def test_search_product():
    response = requests.post(
        "https://automationexercise.com/api/searchProduct",
        data = {"search_product": "Top"}
    )
    assert response.status_code == 200
    data = response.json()
    assert 'products' in data
    assert data['products']
def test_products_list_wrong_method():
    response = requests. post("https://automationexercise.com/api/productsList")
    data = response.json()
    assert data['responseCode'] == 405