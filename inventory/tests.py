from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from inventory.models import Product


# Create your tests here.
class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Laptop",
            description="Asus Laptop high quality product",
            price=50000.00,
            quantity=10
        )
    def test_create_product(self):
        data = {
            "name": "keyboard",
            "description": "black color and small size",
            "price": 500.00,
            "quantity": 20
        }
        url = reverse('product-list-create')
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    def test_list_product(self):
        url = reverse('product-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_single_product_retrieve(self):
        url = reverse('product-detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_upate_product(self):
        url = reverse('product-detail', args=[self.product.id])
        data = {
            "name": "keyboard",
            "description": "black color and small size",
            "price": 500.00,
            "quantity": 20
        }
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_patch_product(self):
        url = reverse('product-detail', args=[self.product.id])
        data = {"quantity": 60}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        url = reverse('product-detail', args=[self.product.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class UserAPITestCase(APITestCase):
    pass




