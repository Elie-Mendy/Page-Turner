from django.urls.base import reverse
from django.test import TestCase


# Create your tests here.


class TestRecommandation2(TestCase):

    def test_recommandation_shoud_return_books(self):
        userList = [
            "11676",
            "197659",
            "46398",
            "230552",
            "269556",
            "270713"
        ]
        for user in userList:
            response = self.client.post(
                reverse("recommandation2", args=(user,))
            )
            content = response.json()["stdout"].split(',')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(len(content) > 0)
        
    
        
    def test_recommandation_shoud_not_return_any_books(self):
        
        response = self.client.post(
            reverse("recommandation2", args=("1111",))
        )
        content = response.json()["stdout"]
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('❌ User NOT FOUND ❌', content)
