from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import Company


class CompanyListViewTest(APITestCase):
    def setUp(self):
        
        Company.objects.create(
            name='Indica Technology',
            icon_url='https://source.unsplash.com/random',
            page_links={'services': 'https://example.com/services'}
        )
        Company.objects.create(
            name='Indica Technology',
            icon_url='https://source.unsplash.com/random',
            page_links={'services': 'https://example.com/services'}
        )

    def test_get_company_list(self):
        
        url = reverse('company-list')

        response = self.client.get(url)

        # Check that the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the expected data structure
        self.assertIn('data', response.data)
        self.assertIn('status', response.data)

        # Check the status value
        self.assertEqual(response.data['status'], status.HTTP_200_OK)

        # Check the content of the 'data' field
        data = response.data['data']
        self.assertEqual(len(data), 2)

        company = data[0]
        self.assertEqual(company['name'], 'Indica Technology')
        self.assertEqual(company['icon_url'],
                         'https://source.unsplash.com/random')
        self.assertEqual(company['page_links'], {
                         'services': 'https://example.com/services'})
