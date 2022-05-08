from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ProductsTestCase(APITestCase):

    def test_all_products(self):
        response = self.client.get("/ecommerce/products")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_detail(self):
        response = self.client.get("/ecommerce/products", kwargs={"pk": 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
class CategoryTestCase(APITestCase):

    def test_all_categories(self):
        response = self.client.get("/ecommerce/categories")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_detail(self):
        response = self.client.get("/ecommerce/categories/2")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class FilterProductsTestCase(APITestCase):
    def test_category_detail(self):
        response = self.client.get("/ecommerce/categories/2/products")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CartTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="ali",
                                             password="password123")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_add_to_cart_authoticated(self):
        self.client.force_authenticate(user=self.user)
        data = {"product": 1,
                    "quantity": 5}
        response = self.client.post("/ecommerce/cart", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_to_cart_unauthoticated(self):
        self.client.force_authenticate(user=None)
        data = {"product": 1,
                    "quantity": 5}
        response = self.client.post("/ecommerce/cart", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_from_cart(self):
        response = self.client.delete("/ecommerce/cart/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)