from django.test import TestCase, Client
import json

class CreateChatTest(TestCase):
    def setup(self):
        self.client = Client()

    def register_and_login(self):
        register_data = json.dumps({"username": "marti",
                            "first_name": "Martin",
                            "last_name": "Dinev",
                            "email": "mars@gmail.com",
                            "password1": "Aa123456",
                            "password2": "Aa123456"})
        self.client.post('/chats/register', register_data, content_type='application/json')
        register_data_2 = json.dumps({"username": "cecko",
                            "first_name": "Martin",
                            "last_name": "Dinev",
                            "email": "mars2@gmail.com",
                            "password1": "Aa123456",
                            "password2": "Aa123456"})
        self.client.post('/chats/register', register_data_2, content_type='application/json')
        login_data = json.dumps({"username": "marti", "password": "Aa123456"})
        self.client.post('/chats/login', login_data, content_type='application/json')

    def test_create_valid_chat(self):
        self.register_and_login()
        chat_data = json.dumps({
            "chat_name": "Gyzariq",
            "members_count": 2,
            "usernames": [
                {"username": "marti"},
                {"username": "cecko"}
            ]
        })
        response = self.client.post('/chats/create-chat', chat_data, content_type='application/json')
        self.assertEqual(json.loads(response.content)["status"], "successful")

    def test_create_duplicate_chat(self):
        self.register_and_login()
        chat_data = json.dumps({
            "chat_name": "Gyzariq",
            "members_count": 2,
            "usernames": [
                {"username": "marti"},
                {"username": "cecko"}
            ]
        })
        self.client.post('/chats/create-chat', chat_data, content_type='application/json')
        response = self.client.post('/chats/create-chat', chat_data, content_type='application/json')
        self.assertEqual(json.loads(response.content)["status"], "unsuccessful")
        self.assertEqual(json.loads(response.content)["error"], "Chat already exists!")

    