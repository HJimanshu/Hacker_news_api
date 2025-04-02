from django.test import TestCase
from unittest.mock import patch
from django.urls import reverse
import requests

# Create your tests here.

class HackerNewsAPITest(TestCase):

    @patch("requests.get")  
    def test_fetch_hackernews_api_data_success(self, mock_get):
    
        mock_get.side_effect = [
            MockResponse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 200),
            MockResponse({
                "title": "Test Story",
                "by": "Test Author",
                "url": "https://test.com",
                "score": 100,
                "time": 1710000000  
            }, 200)
        ] * 10  # Repeat for 10 stories

        response = self.client.get(reverse("fetch_hacker_news"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("data", response.json())
        self.assertEqual(len(response.json()["data"]), 10)
        self.assertEqual(response.json()["data"][0]["title"], "Test Story")

    @patch("requests.get")
    def test_fetch_hackernews_api_data_failure(self, mock_get):
        # Simulate API failure
        mock_get.side_effect = requests.RequestException("API Error")
        
        response = self.client.get(reverse("fetch_hacker_news"))
        self.assertEqual(response.status_code, 500)
        self.assertIn("error", response.json())

# Helper mock class for API responses
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

