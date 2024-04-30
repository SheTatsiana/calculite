from django.test import TestCase
from django.utils import timezone
from datetime import date
from .models import Object, Note, Product, MyObject, MyCurrentObject, WorkDetail
from decimal import Decimal


class ObjectModelTest(TestCase):
    def test_string_representation(self):
        obj = Object(name="Test Object")
        self.assertEqual(str(obj), obj.name)


class NoteModelTest(TestCase):
    def test_string_representation(self):
        note = Note(title="Test Note", date=date.today())
        self.assertEqual(str(note), f"{note.title} ({note.date.strftime('%Y-%m-%d')})")


class ProductModelTest(TestCase):
    def test_string_representation(self):
        product = Product(name="Test Product", price=Decimal('10.50'))
        self.assertEqual(str(product), product.name)


class MyObjectModelTest(TestCase):
    def test_string_representation(self):
        my_object = MyObject(address="Test Address")
        self.assertEqual(str(my_object), my_object.address)

    def test_get_objects_method(self):
        MyObject.objects.create(address="Test Address 1", end_date=date.today())
        MyObject.objects.create(address="Test Address 2", end_date=date.today())
        self.assertEqual(MyObject.get_objects().count(), 2)


class MyCurrentObjectModelTest(TestCase):
    def setUp(self):
        self.my_object = MyObject.objects.create(address="Test Address")
        self.product = Product.objects.create(name="Test Product", price=Decimal('10.50'))
        self.my_current_object = MyCurrentObject.objects.create(my_object=self.my_object)

    def test_string_representation(self):
        self.assertEqual(str(self.my_current_object), str(self.my_object))

    def test_calculate_total_amount_method(self):
        WorkDetail.objects.create(my_current_object=self.my_current_object, product=self.product, quantity=2)
        self.assertEqual(self.my_current_object.calculate_total_amount(), Decimal('21.00'))

    def test_save_method_updates_total_amount(self):
        WorkDetail.objects.create(my_current_object=self.my_current_object, product=self.product, quantity=2)
        self.my_current_object.save()
        self.assertEqual(self.my_current_object.total_amount, Decimal('21.00'))

    def test_get_objects_method(self):
        MyCurrentObject.objects.create(my_object=self.my_object)
        MyCurrentObject.objects.create(my_object=self.my_object)
        self.assertEqual(MyCurrentObject.get_objects().count(), 2)


class WorkDetailModelTest(TestCase):
    def setUp(self):
        self.my_object = MyObject.objects.create(address="Test Address")
        self.product = Product.objects.create(name="Test Product", price=Decimal('10.50'))
        self.my_current_object = MyCurrentObject.objects.create(my_object=self.my_object)

    def test_string_representation(self):
        work_detail = WorkDetail.objects.create(my_current_object=self.my_current_object, product=self.product, quantity=2)
        self.assertEqual(str(work_detail), f"{work_detail.product.name} - {work_detail.quantity} - {work_detail.total_price}")

    def test_save_method_updates_total_price(self):
        work_detail = WorkDetail.objects.create(my_current_object=self.my_current_object, product=self.product, quantity=2)
        self.assertEqual(work_detail.total_price, Decimal('21.00'))
