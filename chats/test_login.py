from django.test import TestCase, Client
import json

# Create your tests here.
class LoginTest(TestCase):
    def setup(self):
        self.client = Client()

    def test_valid_login(self):
        register_data = json.dumps({"username": "marti",
                            "first_name": "Martin",
                            "last_name": "Dinev",
                            "email": "mars@gmail.com",
                            "password1": "Aa123456",
                            "password2": "Aa123456"})
        self.client.post('/chats/register', register_data, content_type='application/json')
        login_data = json.dumps({"username": "marti", "password": "Aa123456"})
        response = self.client.post('/chats/login', login_data, content_type='application/json')
        self.assertEqual(json.loads(response.content)["status"], "successful")

    def test_invalid_login(self):
        register_data = json.dumps({"username": "marti",
                            "first_name": "Martin",
                            "last_name": "Dinev",
                            "email": "mars@gmail.com",
                            "password1": "Aa123456",
                            "password2": "Aa123456"})
        self.client.post('/chats/register', register_data, content_type='application/json')
        login_data = json.dumps({"username": "awdaw", "password": "Aa123456"})
        response = self.client.post('/chats/login', login_data, content_type='application/json')
        self.assertEqual(json.loads(response.content)["status"], "unsuccessful")  