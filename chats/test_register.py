from django.test import TestCase, Client
import json

class RegisterTest(TestCase):
    def setup(self):
        self.client = Client()

    def test_valid_register(self):
        data = json.dumps({"username": "marti",
                            "first_name": "Martin",
                            "last_name": "Dinev",
                            "email": "mars@gmail.com",
                            "password1": "Aa123456",
                            "password2": "Aa123456"})
        response = self.client.post('/chats/register', data, content_type='application/json')
        self.assertEqual(json.loads(response.content)["status"], "successful")

    def test_repeated_username(self):
        data = json.dumps({"username": "marti",
                            "first_name": "Martin",
                            "last_name": "Dinev",
                            "email": "mars@gmail.com",
                            "password1": "Aa123456",
                            "password2": "Aa123456"})
        self.client.post('/chats/register', data, content_type='application/json')
        data2 = json.dumps({"username": "marti",
                            "first_name": "Martin",
                            "last_name": "Dinev",
                            "email": "mars@gmail.com",
                            "password1": "Aa123456",
                            "password2": "Aa123456"})
        response = self.client.post('/chats/register', data2, content_type='application/json')
        self.assertEqual(json.loads(response.content)["status"], "unsuccessful")
        self.assertEqual(json.loads(response.content)["error"], "Username already exist! Please try other username.")
