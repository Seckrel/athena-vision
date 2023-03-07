from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.core.cache import cache


class SettingTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        url = reverse('athenaExt:setting')
        self.response = self.client.get(url)
        self.expected_data = {
            'emotional tone': 0,
            'topic label': 0,
            "blur": 0,
            "strength": '1',
        }

    def test_setting_status_code(self):
        # assuming 'update-setting' is the URL name

        # Assert that the response status code is 200 OK
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

        # Assert that the response data is correct
    def test_setting_response_data(self):

        self.assertEqual(self.response.data, self.expected_data)

        # Assert that the session setting was set correctly
    def test_setting_session_data(self):
        self.assertEqual(
            self.client.session['blur'], self.expected_data["blur"])
        self.assertEqual(
            self.client.session['emotional tone'], self.expected_data["emotional tone"])
        self.assertEqual(
            self.client.session['topic label'], self.expected_data["topic label"])
        self.assertEqual(
            self.client.session['strength'], self.expected_data["strength"])

        # Assert that the cache value was set correctly
    def test_setting_cache(self):
        self.assertEqual(cache.get('ext_power'), 0)


class ExtPowerSettingTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        url = reverse('athenaExt:extpower')
        self.data = {
            'extFlag': True
        }
        self.response = self.client.post(url, self.data, format='json')

    def test_ext_status(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_response_data(self):
        self.assertEqual(self.response.data['blur'], 1)
        self.assertEqual(self.response.data['extOn'], True)
        self.assertEqual(self.response.data['strength'], '1')

    def test_session(self):
        self.assertTrue(self.client.session['ext_power'])
        self.assertEqual(self.client.session['blur'], 1)
        self.assertEqual(self.client.session['emotional tone'], 1)
        self.assertEqual(self.client.session['topic label'], 1)
        self.assertEqual(self.client.session['strength'], '1')
