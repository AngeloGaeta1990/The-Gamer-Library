from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Platform


class TestLibraryViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.client.login(username='testuser', password='testpassword')
        self.platform = Platform(name="Test PC", user=self.user,
                                 slug="test-pc", category="PC")

        self.platform.save()

    def test_render_platform_detail_page(self):
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.get(reverse(
            'platform_detail', args=[self.user.id, self.platform.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test PC", response.content)
        self.assertIn(b"PC", response.content)

    def test_add_platform_(self):
        """Test for posting a platform on a post"""
        self.client.login(
            username="myUsername", password="myPassword")
        platform_data = {
            "name": "Test PC",
            "user": self.user.id,
            "slug": "test-pc",
            "category": "PC"
        }
        response = self.client.get(reverse(
            'platform_detail', args=[self.user.id, self.platform.slug]),
                                    platform_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Test PC',
            response.content
        )
