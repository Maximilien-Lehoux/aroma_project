# -*- coding: utf-8 -*-

from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Pathology, EssentialOil, VegetableOil, Recipe, Way, \
    NeutralProduct, MethodOfUse, SideEffect, Contraindication


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
        self.way_test = Way.objects.create(name="cutanée")
        self.way_test.save()
        self.way_test.pathology.add(self.pathology_test)

        self.essential_oil_test = EssentialOil.objects.create(
            name="Laurier noble",
            image="laurier_noble.jpg"
        )
        self.essential_oil_test.save()
        self.essential_oil_test.pathology.add(self.pathology_test)
        self.way_test.essential_oil.add(self.essential_oil_test)

        self.methode_use_test = MethodOfUse.objects.create(
            name="cutanée générale",
            description="test",
            quantity="2/jour",
        )
        self.methode_use_test.save()

        self.amount_test = Recipe.objects.create(
            name="1 he cutanée",
            number_he=1,
            amount_he="30 gouttes",
            mount_hv="15 ml",
            way_id=self.way_test.id,
        )
        self.amount_test.save()

        self.user_admin = User.objects.create(username='Arthur', last_name='H',
                                        email='arthurH@gmail.com',
                                        is_staff=True)
        self.user_admin.set_password('1234')
        self.user_admin.save()

        self.user = User.objects.create(username='Merlin', last_name='M',
                                        email='merlin@gmail.com')
        self.user.set_password('5678')
        self.user.save()

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

    def test_advice_without_administration_route(self):
        data = {"pathology_choose": self.pathology_test,
                "way_choose": ""}
        response = self.client.post(reverse('advice:advice_he'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'advice/advice.html')

    def test_advice_with_administration_route(self):
        data = {"pathology_choose": self.pathology_test,
                "way_choose": self.way_test}
        response = self.client.post(reverse('advice:advice_he'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'advice/advice.html')

    def test_display_admin_database_return_200_with_user_admin(self):
        self.client.login(username="Arthur", password="1234")
        response = self.client.get(reverse('advice:admin_database'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'advice/admin_database.html')

    def test_display_admin_database_return_302_without_user_admin(self):
        self.client.login(username="Merlin", password="5678")
        response = self.client.get(reverse('advice:admin_database'))
        self.assertEqual(response.status_code, 302)

    def test_display_admin_database_return_302_with_logout(self):
        self.client.logout()
        response = self.client.get(reverse('advice:admin_database'))
        self.assertEqual(response.status_code, 302)


