from django.test import TestCase
from django.urls import reverse


class HomeTestCase(TestCase):
    def test_home_view(self):
        url = reverse("twitter_stream:home")  # get the URL for the home view
        response = self.client.get(url)  # make a GET request to the URL
        # make sure the response is OK
        self.assertEqual(response.status_code, 200)
