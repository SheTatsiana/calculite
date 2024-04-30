from django.test import TestCase, Client
from django.urls import reverse
from .models import Object, MyObject, MyCurrentObject, Product, Note
from .forms import MyObjectForm, MyCurrentObjectForm

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_add_item_view(self):
        response = self.client.get(reverse('add_item'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_item.html')

    def test_add_new_view_GET(self):
        response = self.client.get(reverse('add_new'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_new.html')

    def test_add_new_view_POST(self):
        response = self.client.post(reverse('add_new'))
        self.assertEquals(response.status_code, 200)  # Вам нужно обработать форму, чтобы этот тест сработал корректно

    def test_catalog_view(self):
        response = self.client.get(reverse('catalog'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog.html')

    def test_my_object_view(self):
        response = self.client.get(reverse('my_object'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_object.html')

    def test_profile_view(self):
        response = self.client.get(reverse('profile'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_create_note_view_GET(self):
        response = self.client.get(reverse('create_note'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_note.html')

    def test_create_note_view_POST(self):
        response = self.client.post(reverse('create_note'), {'title': 'Test Note', 'content': 'Test Content'})
        self.assertEquals(response.status_code, 302)  # Перенаправление

    # Добавьте тесты для классов ProductListView и ProductDetailView, если они нужны

    def test_mycurrentobject_view(self):
        response = self.client.get(reverse('mycurrentobject'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mycurrentobject.html')

    def test_my_current_object_detail_view(self):
        my_current_object = MyCurrentObject.objects.create()
        response = self.client.get(reverse('my_current_object_detail', args=[my_current_object.id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mycurrentobjectdetail.html')

    # Добавьте тесты для my_current_objects_view и create_object, если они нужны
