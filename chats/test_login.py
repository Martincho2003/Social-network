from django.test import TestCase, Client
import json

# Create your tests here.
class LoginTest(TestCase):
    def setup(self):
        self.client = Client()

    # def test_valid_login(self):
    #     data = json.dumps({"username": "marti", "password": "Aa123456"})
    #     response = self.client.post('/chats/login', data, content_type='application/json')
    #     self.assertEqual(json.loads(response.content)["status"], "successful")  