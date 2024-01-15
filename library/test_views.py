from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import AddPlatformForm
from .models import Platform

class TestLibraryViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.platform = Platform(name="Test PC", user=self.user,
                         slug="test-pc")
        self.platform.save()

    def test_render_platform_detail_page(self):
        response = self.client.get(reverse(
            'platform_detail', args=['platform-name']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"platform name", response.content)
        self.assertIn(b"platform category", response.content)
        