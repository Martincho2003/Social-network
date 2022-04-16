from django.test import TestCase, Client
import json

class ListChatTest(TestCase):
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
        register_data = json.dumps({"username": "marto",
                            "first_name": "Martin",
                            "last_name": "Dinev",
                            "email": "mars3@gmail.com",
                            "password1": "Aa123456",
                            "password2": "Aa123456"})
        self.client.post('/chats/register', register_data, content_type='application/json')
        login_data = json.dumps({"username": "marti", "password": "Aa123456"})
        self.client.post('/chats/login', login_data, content_type='application/json')

    def create_chat(self, chat_name):
        self.register_and_login()
        chat_data = json.dumps({
            "chat_name": chat_name,
            "members_count": 2,
            "usernames": [
                {"username": "marti"},
                {"username": "cecko"}
            ]
        })
        self.client.post('/chats/create-chat', chat_data, content_type='application/json')

    def test_add_user_to_chat(self):
        self.create_chat("Chat1")
        new_user_data = json.dumps({
            "chat_name": "Chat1",
            "chat_owner_id": 1,
            "username": "marto"
        })
        response = self.client.post('/chats/add-user-to-chat', new_user_data, content_type='application/json')
        response = json.loads(response.content)
        self.assertEqual(response["status"], "successful")

    