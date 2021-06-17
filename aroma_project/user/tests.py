# -*- coding: utf-8 -*-

from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User


class TestViewsUser(TestCase):
    def setUp(self):
        pass

    def test_contact_page_return_200(self):
        """test that the user page returns a 200"""
        response = self.client.get(reverse('user:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/contact.html')

    def test_request_post_contact(self):
        """test that the user page returns a 302"""
        data = {"first_name": "Maximilen",
                "last_name": "Lehoux",
                "email_address": "maximilien.lehoux@gmail.com",
                "message": "Que peux t-on donner "
                           "aux bébé de 6 mois pour dormir ?"}
        response = self.client.post(reverse('user:contact'), data)
        self.assertEqual(response.status_code, 302)

    def test_request_post_without_last_name_contact(self):
        """test that the user page returns a 200"""
        data = {"first_name": "Maximilen",
                "last_name": "",
                "email_address": "maximilien.lehoux@gmail.com",
                "message": "Que peux t-on donner "
                           "aux bébé de 6 mois pour dormir ?"}
        response = self.client.post(reverse('user:contact'), data)
        self.assertEqual(response.status_code, 200)

    def test_request_post_without_first_name_contact(self):
        """test that the user page returns a 200"""
        data = {"first_name": "",
                "last_name": "Lehoux",
                "email_address": "maximilien.lehoux@gmail.com",
                "message": "Que peux t-on donner "
                           "aux bébé de 6 mois pour dormir ?"}
        response = self.client.post(reverse('user:contact'), data)
        self.assertEqual(response.status_code, 200)

    def test_request_post_without_email_address_contact(self):
        """test that the user page returns a 200"""
        data = {"first_name": "Maximilien",
                "last_name": "Lehoux",
                "email_address": "",
                "message": "Que peux t-on donner "
                           "aux bébé de 6 mois pour dormir ?"}
        response = self.client.post(reverse('user:contact'), data)
        self.assertEqual(response.status_code, 200)

    def test_request_post_without_message_contact(self):
        """test that the user page returns a 200"""
        data = {"first_name": "Maximilien",
                "last_name": "Lehoux",
                "email_address": "maximilien.lehoux@gmail.com",
                "message": ""}
        response = self.client.post(reverse('user:contact'), data)
        self.assertEqual(response.status_code, 200)



