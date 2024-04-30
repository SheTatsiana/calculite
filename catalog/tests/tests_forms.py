from django.test import TestCase
from .forms import MyObjectForm, MyCurrentObjectForm
from .models import MyObject, MyCurrentObject

class TestForms(TestCase):

    def test_my_object_form_valid_data(self):
        form = MyObjectForm(data={
            'name': 'Test Object',
            'description': 'Test Description'
        })

        self.assertTrue(form.is_valid())

    def test_my_object_form_no_data(self):
        form = MyObjectForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_my_current_object_form_valid_data(self):
        form = MyCurrentObjectForm(data={
            'name': 'Test Current Object',
            'description': 'Test Current Description'
        })

        self.assertTrue(form.is_valid())

    def test_my_current_object_form_no_data(self):
        form = MyCurrentObjectForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
