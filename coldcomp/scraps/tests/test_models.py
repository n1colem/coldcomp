from django.test import TestCase

from scraps.models import Scrap, Mood


class ModelsTestCast(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.scrap1 = Scrap.objects.create(
            title = 'TestTitle',
            slug = 'test-slug',
            body = 'test test test')
        cls.mood1 = Mood.objects.create(
            title = 'shy',
            color = 'CF6')

    def test_scrap_model(self):
        self.assertEqual(repr(self.scrap1), '<Scrap 1: TestTitle>')

    def test_scrap_model(self):
        self.assertEqual(str(self.scrap1), 'TestTitle')

    def test_mood_model(self):
        self.assertEqual(repr(self.mood1), '<Mood 1: shy>')

    def test_mood_model(self):
        self.assertEqual(str(self.mood1), 'shy')
