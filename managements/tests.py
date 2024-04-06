from django.test import TestCase
from django.urls import reverse
from .models import Bus
import datetime

class BusModelAndViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Creating two buses for testing
        cls.bus1 = Bus.objects.create(
            name='Test Bus 1',
            color='Red',
            no_plate='ABC123',
            seats=50,
            departure_city='Nairobi',
            arrival_city='Mombasa',
            departure_time=datetime.date(2024, 3, 1),
            depart_time=datetime.time(8, 0)
        )
        cls.bus2 = Bus.objects.create(
            name='Test Bus 2',
            color='Blue',
            no_plate='XYZ789',
            seats=40,
            departure_city='Mombasa',
            arrival_city='Nairobi',
            departure_time=datetime.date(2024, 4, 1),
            depart_time=datetime.time(9, 0)
        )

    def test_search_form_view_get(self):
        # Test the search_form view with a GET request
        response = self.client.get(reverse('search_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_form.html')

    # def test_bus_detail_view_get(self):
    #     # Test the bus_detail view with an existing bus ID
    #     response = self.client.get(reverse('bus_detail', args=[self.bus1.pk]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'bus_detail.html')

    # Add more tests as necessary for your application
