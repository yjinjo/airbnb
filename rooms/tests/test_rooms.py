from rest_framework.test import APITestCase
from users.models import User


class TestRoom(APITestCase):
    def setUp(self):
        user = User.objects.create(
            username="test",
        )
        user.set_password("test1234!")
        user.save()

        self.user = user

    def test_create_room(self):
        response = self.client.post("/api/v1/rooms/")

        self.assertEqual(response.status_code, 403)

        self.client.force_login(self.user)

        response = self.client.post("/api/v1/rooms/")
        print(response.json())
