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

    def test_list_chats(self):
        self.create_chat("Chat1")
        self.create_chat("Chat2")
        response = self.client.get('/chats/chats-list', content_type='application/json')
        response = json.loads(response.content)
        self.assertEqual(response["chats"][0]["chat_name"], "Chat1")
        self.assertEqual(response["chats"][0]["chat_owner_id"], 1)
        members0 = []
        for member in response["chats"][0]["chat_members"]:
            members0.append(member["username"])
        self.assertTrue("marti" in members0)
        self.assertTrue("cecko" in members0)
        self.assertEqual(response["chats"][1]["chat_name"], "Chat2")
        self.assertEqual(response["chats"][1]["chat_owner_id"], 1)
        members1 = []
        for member in response["chats"][1]["chat_members"]:
            members1.append(member["username"])
        self.assertTrue("marti" in members1)
        self.assertTrue("cecko" in members1)

    