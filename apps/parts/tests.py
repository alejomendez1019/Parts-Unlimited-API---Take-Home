from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Part
from .serializers import PartSerializer


class PartViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.part_data = {
            'name': 'Test Part',
            'sku': 'TESTSKU',
            'description': 'Test Description',
            'weight_ounces': 10,
            'is_active': True
        }
        self.part = Part.objects.create(**self.part_data)
        self.valid_payload = {
            'name': 'New Part',
            'sku': 'NEWSKU',
            'description': 'New Description',
            'weight_ounces': 20,
            'is_active': True
        }
        self.invalid_payload = {
            'name': '',
            'sku': 'INVALIDSKU',
            'description': 'Invalid Description',
            'weight_ounces': -10,
            'is_active': True
        }

    def test_create_valid_part(self):
        response = self.client.post('/api/parts/', data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Part.objects.count(), 2)
        self.assertEqual(response.data['name'], self.valid_payload['name'])

    def test_create_invalid_part(self):
        response = self.client.post('/api/parts/', data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_parts(self):
        response = self.client.get('/api/parts/')
        parts = Part.objects.all()
        serializer = PartSerializer(parts, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_part(self):
        response = self.client.get(f'/api/parts/{self.part.id}/')
        part = Part.objects.get(id=self.part.id)
        serializer = PartSerializer(part)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_part(self):
        response = self.client.put(f'/api/parts/{self.part.id}/', data=self
                                   .valid_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.valid_payload['name'])

    def test_delete_part(self):
        response = self.client.delete(f'/api/parts/{self.part.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Part.objects.count(), 0)


class CommonWordsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.part_data = [
            {'name': 'Part1', 'sku': 'SKU1', 'description': 'Test description one', 'weight_ounces': 10, 'is_active': True},
            {'name': 'Part2', 'sku': 'SKU2', 'description': 'Test description two', 'weight_ounces': 15, 'is_active': True},
            {'name': 'Part3', 'sku': 'SKU3', 'description': 'Another test description', 'weight_ounces': 20, 'is_active': True},
            {'name': 'Part4', 'sku': 'SKU4', 'description': 'This part is amazing and fantastic', 'weight_ounces': 5, 'is_active': True},
            {'name': 'Part5', 'sku': 'SKU5', 'description': 'Description with common words common words', 'weight_ounces': 25, 'is_active': True},
            {'name': 'Part6', 'sku': 'SKU6', 'description': 'Testing the common word finder function', 'weight_ounces': 30, 'is_active': True},
        ]
        for part in self.part_data:
            Part.objects.create(**part)

    def test_get_common_words(self):
        # Test basic functionality

        response = self.client.get('/api/parts/common-words/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('common_words' in response.data)
        # Check that common_words has the expected structure
        self.assertIsInstance(response.data['common_words'], dict)
        # Check that common_words has at least one word
        self.assertGreaterEqual(len(response.data['common_words']), 1)

    def test_get_common_words_no_data(self):
        # test when there are no parts or descriptions in the database

        Part.objects.all().delete()
        response = self.client.get('/api/parts/common-words/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, {'message': 'No descriptions found'})

    def test_get_common_words_empty_descriptions(self):
        # test when there are parts in the database but no words in the descriptions
        Part.objects.all().delete()
        Part.objects.create(name='Part4', sku='SKU4', description='', weight_ounces=5, is_active=True)
        response = self.client.get('/api/parts/common-words/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, {'message': 'No words found in descriptions'})
