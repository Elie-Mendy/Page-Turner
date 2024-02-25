from django.urls.base import reverse
from django.test import TestCase


# Create your tests here.


class TestRecommandation(TestCase):

    def test_recommandation_shoud_return_books(self):

        response = self.client.post(reverse("recommandation", args=("Harry Potter",)))
        content = response.json()["stdout"].split(",")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(content) > 0)

    def test_recommandation_shoud_not_return_any_books(self):

        response = self.client.post(reverse("recommandation", args=("WrongValue1234",)))
        content = response.json()["stdout"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual("❌ COULD NOT FIND ❌", content)
