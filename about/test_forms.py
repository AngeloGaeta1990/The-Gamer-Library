from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Asdrubale',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_missing_name(self):
        """ Test for is invalid if name is missing"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form is valid even if name is missing")

    def test_form_missing_email(self):
        """ Test for is invalid if email is missing"""
        form = CollaborateForm({
            'name': 'Asdrubale',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form is valid even if e-mail is missing")

    def test_form_missing_message(self):
        """ Test for is invalid if email is missing"""
        form = CollaborateForm({
            'name': 'Asdrubale',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Form is valid even if message is missing")