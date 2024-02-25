from django.urls.base import reverse
from django.test import TestCase


# Create your tests here.


class TestRecommandation2(TestCase):

    def test_recommandation_shoud_return_books(self):
        userList = [
            "11676",
            "197659",
            "156269",
            "88733",
            "31315",
            "69078"
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


"""
EXHAUSTIVE LIST OF USERS WITH BOOKS
11676
197659
46398
230522
7346
13552
31315
78973
107784
216683
105517
129716
31826
37950
56399
93047
114988
234828
252695
16795
135149
177432
23902
31556
76626
89602
95359
110934
123883
129074
147847
171118
174304
200226
25981
60244
69078
204864
104636
110973
236283
35859
38273
56959
30276
98391
114368
153662
156467
158295
258185
162639
240144
269566
177458
68555
112001
128835
6251
76499
265115
6575
60707
101851
270713
189835
249894
51883
225087
79441
254206
75591
88733
140358
16634
97874
87141
156150
172742
217740
36606
190925
225763
261829
274061
43246
156269
55490
182085
257204
135265
235105
168245
30511
23768
185233
142524
81560
254899
248718
264321
100906
130554
212965
262998
162052
23872
78553
265889
25409
88677
216012
94347
242006
189334
69697
4385
63714
"""