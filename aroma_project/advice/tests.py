from django.urls import reverse
from django.test import TestCase

from.models import Pathology, Way, VegetableOil


class TestViewsAdvice(TestCase):
    def setUp(self):
        self.vegetable_oil_test = VegetableOil.objects.create(
            name="noyau d'abricot",
            type="fluide",
            image="noyau_abricot.png")
        self.vegetable_oil_test.save()
        self.vegetable_oil_test_id = self.vegetable_oil_test.pk

        self.pathology_test = Pathology.objects.create(
            name="rhume",
            zone="general",
            vegetable_oil_id=self.vegetable_oil_test_id)
        self.pathology_test.save()
        self.way_test = Way.objects.create(name="cutanee")
        self.way_test.save()
        self.pathology_test.way.add(self.way_test)

    def test_index_page_return_200(self):
        """test that the index page returns a 200"""
        response = self.client.get(reverse('advice:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'advice/index.html')

    def test_index_page_return_302(self):
        response = self.client.post(reverse('advice:index'))
        self.assertEqual(response.status_code, 302)

    def test_advice_return_200(self):
        data = {"pathology_choose": self.pathology_test}
        response = self.client.post(reverse('advice:advice_he'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'advice/advice.html')

