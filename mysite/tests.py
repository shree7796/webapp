from django.test import TestCase

# Create your tests here.
from .myapp.models import PersonalDetailsModel


class ModelTestCase(TestCase):
    def setUp(self):
        PersonalDetailsModel.objects.create(name="lion", sound="roar")
        PersonalDetailsModel.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = PersonalDetailsModel.objects.get(name="lion")
        cat = PersonalDetailsModel.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
