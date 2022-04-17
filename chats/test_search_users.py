from django.test import TestCase, Client
import json

class SearchUsers(TestCase):
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
        register_data = json.dumps({"username": "cecko",
                            "first_name": "Martin",
                            "last_name": "Dinev",
                            "email": "mars2@gmail.com",
                            "password1": "Aa123456",
                            "password2": "Aa123456"})
        self.client.post('/chats/register', register_data, content_type='application/json')
        register_data = json.dumps({"username": "marto",
                            "first_name": "Martin",
                            "last_name": "Dinev",
                            "email": "mars3@gmail.com",
                            "password1": "Aa123456",
                            "password2": "Aa123456"})
        self.client.post('/chats/register', register_data, content_type='application/json')
        login_data = json.dumps({"username": "marti", "password": "Aa123456"})
        self.client.post('/chats/login', login_data, content_type='application/json')

    def test_search_users(self):
        self.register_and_login()
        search_data = json.dumps({"string": "ma"})
        response = self.client.generic('GET', '/chats/search-user', data=search_data, content_type='application/json')
        response = json.loads(response.content)
        users = []
        for user in response["users"]:
            users.append(user["username"])
        self.assertEqual(len(users), 2)
        self.assertTrue("marto" in users)
        self.assertTrue("marti" in users)

    def test_search_users_ignoring_case(self):
        self.register_and_login()
        search_data = json.dumps({"string": "Ma"})
        response = self.client.generic('GET', '/chats/search-user', data=search_data, content_type='application/json')
        response = json.loads(response.content)
        users = []
        for user in response["users"]:
            users.append(user["username"])
        self.assertEqual(len(users), 2)
        self.assertTrue("marto" in users)
        self.assertTrue("marti" in users)

    