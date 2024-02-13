from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Platform
from .forms import EditPlatformForm


class TestLibraryViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.client.login(username='myUsername', password='testpassword')
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

    def test_add_platform(self):
        """Test for posting a platform on a post"""
        self.client.login(
            username="myUsername", password="myPassword")
        platform_data = {
            "name": "Test PC",
            "user": self.user.id,
            "slug": "test-pc",
            "category": "PC"
        }
        response = self.client.post(reverse(
            'platform_detail', args=[self.user.id, self.platform.slug]),
                                    platform_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Test PC',
            response.content
        )

    def test_platform_list_view(self):
        self.client.login(
            username="myUsername", password="myPassword")
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/index.html')
        self.assertQuerysetEqual(response.context['platforms'],
                                 Platform.objects.filter(user=self.user),
                                 transform=lambda x: x)

    def test_edit_platform_view(self):
        self.client.login(
            username="myUsername", password="myPassword")
        response = self.client.get(reverse('edit_platform',
                                           args=[self.user.id,
                                                 self.platform.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/edit_platform_form.html')
        self.assertIsInstance(response.context['edit_platform_form'],
                              EditPlatformForm)

        # Test submitting the form with valid data
        updated_data = {
            'name': 'Updated PC',
            'category': 'pc'
        }
        response = self.client.post(reverse('edit_platform',
                                            args=[self.user.id,
                                                  self.platform.slug]),
                                    updated_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.platform.refresh_from_db()
        self.assertEqual(self.platform.name, 'Updated PC')

    def test_delete_platform_view(self):
        self.client.login(username="myUsername", password="myPassword")
        # Test submitting the form (POST request)
        response = self.client.post(reverse('delete_platform',
                                            args=[self.user.id,
                                                  self.platform.slug]))

        # After successful deletion, the view should redirect to 'home'
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        # Check that the platform is no longer in the database
        self.assertFalse(Platform.objects.filter(pk=self.platform.pk).exists())
