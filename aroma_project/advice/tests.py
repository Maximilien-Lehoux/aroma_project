# -*- coding: utf-8 -*-

from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Pathology, EssentialOil, VegetableOil, Recipe, Way, \
    NeutralProduct, MethodOfUse, SideEffect, Contraindication


class TestViewsAdvice(TestCase):
    def setUp(self):
        self.vegetable_oil_test = VegetableOil.objects.create(
            name="huile de noyau d'abricot",
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

        self.way_test2 = Way.objects.create(name="orale")
        self.way_test3 = Way.objects.create(name="bain")
        self.way_test4 = Way.objects.create(name="diffusion")
        self.way_test5 = Way.objects.create(name="Inhalation")

        self.way_test2.save()
        self.way_test3.save()
        self.way_test4.save()
        self.way_test5.save()

        self.way_test2.pathology.add(self.pathology_test)
        self.way_test3.pathology.add(self.pathology_test)
        self.way_test4.pathology.add(self.pathology_test)
        self.way_test5.pathology.add(self.pathology_test)

        self.neutral_product = NeutralProduct.objects.create(
            name="miel",
            image="miel.png")
        self.neutral_product2 = NeutralProduct.objects.create(
            name="gel douche",
            image="gel_douche.png")
        self.neutral_product3 = NeutralProduct.objects.create(
            name="alcool",
            image="alcool.png")
        self.neutral_product4 = NeutralProduct.objects.create(
            name="bol d'eau",
            image="eau.png")

        self.neutral_product.save()
        self.neutral_product2.save()
        self.neutral_product3.save()
        self.neutral_product4.save()

        self.essential_oil_test = EssentialOil.objects.create(
            name="Laurier noble",
            image="laurier_noble.jpg"
        )
        self.essential_oil_test.save()
        self.essential_oil_test.pathology.add(self.pathology_test)
        self.way_test.essential_oil.add(self.essential_oil_test)
        self.way_test2.essential_oil.add(self.essential_oil_test)
        self.way_test3.essential_oil.add(self.essential_oil_test)
        self.way_test4.essential_oil.add(self.essential_oil_test)
        self.way_test5.essential_oil.add(self.essential_oil_test)

        self.essential_oil2_test = EssentialOil.objects.create(
            name="Gaulthérie",
            image="Gaulthérie.jpg"
        )
        self.essential_oil2_test.save()
        self.way_test.essential_oil.add(self.essential_oil2_test)

        self.essential_oil3_test = EssentialOil.objects.create(
            name="Ravintsara",
            image="Ravintsara.jpg"
        )
        self.essential_oil3_test.save()
        self.way_test.essential_oil.add(self.essential_oil3_test)

        self.methode_use_test = MethodOfUse.objects.create(
            name="cutanée générale",
            description="test",
            quantity="2/jour",
        )
        self.methode_use_test2 = MethodOfUse.objects.create(
            name="cutanée",
            description="test",
            quantity="2/jour",
        )
        self.methode_use_test3 = MethodOfUse.objects.create(
            name="orale",
            description="test",
            quantity="2/jour",
        )
        self.methode_use_test4 = MethodOfUse.objects.create(
            name="diffusion",
            description="test",
            quantity="2/jour",
        )
        self.methode_use_test5 = MethodOfUse.objects.create(
            name="inhalation",
            description="test",
            quantity="2/jour",
        )
        self.methode_use_test6 = MethodOfUse.objects.create(
            name="bain",
            description="test",
            quantity="2/jour",
        )

        self.methode_use_test.save()
        self.methode_use_test2.save()
        self.methode_use_test3.save()
        self.methode_use_test4.save()
        self.methode_use_test5.save()
        self.methode_use_test6.save()

        self.amount_test = Recipe.objects.create(
            name="1 he cutanée",
            number_he=1,
            amount_he="30 gouttes",
            mount_hv="15 ml",
            way_id=self.way_test.id,
        )
        self.amount_test.save()

        self.amount_test2 = Recipe.objects.create(
            name="1 he orale",
            number_he=1,
            amount_he="30 gouttes",
            mount_hv="15 ml",
            way_id=self.way_test2.id,
        )
        self.amount_test2.save()

        self.amount_test3 = Recipe.objects.create(
            name="1 he bain",
            number_he=1,
            amount_he="30 gouttes",
            mount_hv="15 ml",
            way_id=self.way_test3.id,
        )
        self.amount_test3.save()

        self.amount_test4 = Recipe.objects.create(
            name="1 he diffusion",
            number_he=1,
            amount_he="30 gouttes",
            mount_hv="15 ml",
            way_id=self.way_test4.id,
        )
        self.amount_test4.save()

        self.amount_test5 = Recipe.objects.create(
            name="1 he inhalation",
            number_he=1,
            amount_he="30 gouttes",
            mount_hv="15 ml",
            way_id=self.way_test5.id,
        )
        self.amount_test5.save()

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

    def test_advice_with_administration_route1(self):
        data = {"pathology_choose": self.pathology_test,
                "way_choose": self.way_test}
        response = self.client.post(reverse('advice:advice_he'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'advice/advice.html')

    def test_advice_with_administration_route2(self):
        data = {"pathology_choose": self.pathology_test,
                "way_choose": self.way_test2}
        response = self.client.post(reverse('advice:advice_he'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'advice/advice.html')

    def test_advice_with_administration_route3(self):
        data = {"pathology_choose": self.pathology_test,
                "way_choose": self.way_test3}
        response = self.client.post(reverse('advice:advice_he'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'advice/advice.html')

    def test_advice_with_administration_route4(self):
        data = {"pathology_choose": self.pathology_test,
                "way_choose": self.way_test4}
        response = self.client.post(reverse('advice:advice_he'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'advice/advice.html')

    def test_advice_with_administration_route5(self):
        data = {"pathology_choose": self.pathology_test,
                "way_choose": self.way_test5}
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

    def test_try_new_pathology_saved_without_pathology(self):
        self.client.login(username="Arthur", password="1234")
        old_db_pathology_saved = Pathology.objects.count()
        data = {"pathology": "",
                "zone": "gorge",
                "vegetable_oil": self.vegetable_oil_test.name,
                "essential_oil1": self.essential_oil_test.name,
                "essential_oil2": "",
                "essential_oil3": ""}
        response = self.client.post(reverse('advice:admin_database'), data)
        new_db_pathology_saved = Pathology.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(old_db_pathology_saved, new_db_pathology_saved)

    def test_try_new_pathology_saved_without_zone(self):
        self.client.login(username="Arthur", password="1234")
        old_db_pathology_saved = Pathology.objects.count()
        data = {"pathology": "angine",
                "zone": "",
                "vegetable_oil": self.vegetable_oil_test.name,
                "essential_oil1": self.essential_oil_test.name,
                "essential_oil2": "",
                "essential_oil3": ""}
        response = self.client.post(reverse('advice:admin_database'), data)
        new_db_pathology_saved = Pathology.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(old_db_pathology_saved, new_db_pathology_saved)

    def test_try_new_pathology_saved_without_vegetable_oil(self):
        self.client.login(username="Arthur", password="1234")
        old_db_pathology_saved = Pathology.objects.count()
        data = {"pathology": "angine",
                "zone": "gorge",
                "vegetable_oil": "",
                "essential_oil1": self.essential_oil_test.name,
                "essential_oil2": "",
                "essential_oil3": ""}
        response = self.client.post(reverse('advice:admin_database'), data)
        new_db_pathology_saved = Pathology.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(old_db_pathology_saved, new_db_pathology_saved)

    def test_try_new_pathology_saved_without_essential_oil(self):
        self.client.login(username="Arthur", password="1234")
        old_db_pathology_saved = Pathology.objects.count()
        data = {"pathology": "angine",
                "zone": "gorge",
                "vegetable_oil": self.vegetable_oil_test,
                "essential_oil1": "",
                "essential_oil2": "",
                "essential_oil3": ""}
        response = self.client.post(reverse('advice:admin_database'), data)
        new_db_pathology_saved = Pathology.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(old_db_pathology_saved, new_db_pathology_saved)

    def test_try_new_pathology_with_one_he(self):
        self.client.login(username="Arthur", password="1234")
        old_db_pathology_saved = Pathology.objects.count()
        data = {"pathology": "angine",
                "zone": "gorge",
                "vegetable_oil": self.vegetable_oil_test,
                "essential_oil1": self.essential_oil_test,
                "essential_oil2": "",
                "essential_oil3": ""}
        response = self.client.post(reverse('advice:admin_database'), data)
        new_db_pathology_saved = Pathology.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(old_db_pathology_saved + 1, new_db_pathology_saved)

    def test_try_new_pathology_with_two_he(self):
        self.client.login(username="Arthur", password="1234")
        old_db_pathology_saved = Pathology.objects.count()
        data = {"pathology": "Ongle incarné",
                "zone": "gorge",
                "vegetable_oil": self.vegetable_oil_test,
                "essential_oil1": self.essential_oil_test,
                "essential_oil2": self.essential_oil2_test,
                "essential_oil3": ""}
        response = self.client.post(reverse('advice:admin_database'), data)
        new_db_pathology_saved = Pathology.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(old_db_pathology_saved + 1, new_db_pathology_saved)

    def test_try_new_pathology_with_three_he(self):
        self.client.login(username="Arthur", password="1234")
        old_db_pathology_saved = Pathology.objects.count()
        data = {"pathology": "mycose",
                "zone": "Ongle",
                "vegetable_oil": self.vegetable_oil_test,
                "essential_oil1": self.essential_oil_test,
                "essential_oil2": self.essential_oil2_test,
                "essential_oil3": self.essential_oil3_test}
        response = self.client.post(reverse('advice:admin_database'), data)
        new_db_pathology_saved = Pathology.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(old_db_pathology_saved + 1, new_db_pathology_saved)