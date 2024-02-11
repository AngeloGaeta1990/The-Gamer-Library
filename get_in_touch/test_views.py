from django.test import TestCase
from django.urls import reverse
from .models import Bio
from .forms import CollaborateForm
# Create your tests here.


class TestLibraryViews(TestCase):

    def setUp(self):
        """
        Creates Bio instance
        """
        self.bio = Bio(title="Get in touch test",
                       description="Get in touch test description")
        self.bio.save()

    def test_render_get_in_touch_page(self):
        """
        Verifies get request contains bio title and description
        """
        response = self.client.get(reverse(
            'get_in_touch', ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Get in touch test", response.content)
        self.assertIn(b"Get in touch test description", response.content)

    def test_collaborate_view(self):
        """
        Verifies rendering collaborate template and form instance in context
        """
        response = self.client.get(reverse('collaborate'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('collaborate_form', response.context)
        self.assertIsInstance(response.context['collaborate_form'],
                              CollaborateForm)

    def test_collaboration_post(self):
        """Test for sending a collaboration request"""
        collaboration_data = {
            "name": "Jeff Bezos",
            "email": "myemail@provider.com",
            "message": "I want to collaborate for an awesome project",
        }
        response = self.client.post(reverse(
            'collaborate'), collaboration_data, follow=True)
        self.assertIn(
            b'collaboration request sent',
            response.content)
