import datetime
import pickle
import numpy as np
import tensorflow as tf
import os
from django.conf import settings

from django.test import TestCase
from rest_framework import serializers
# Create your tests here.


class TestComment(TestCase):

    def setUp(self) -> None:

        # import text vectorization layer
        from_disk = pickle.load(
            open(str(settings.BASE_DIR) + "/comment/utils/tv_layer.pkl", "rb"))
        self.vectorizer = tf.keras.layers.TextVectorization.from_config(
            from_disk['config'])

        # vectorizer adaptation with some dummy data (BUG in Keras)
        self.vectorizer.adapt(tf.data.Dataset.from_tensor_slices(["xyz"]))
        self.vectorizer.set_weights(from_disk['weights'])

        # model instatiation
        self.model = tf.keras.models.load_model(
            str(settings.BASE_DIR) + '/comment/utils/newModel.h5')

    def test_comment_should_pass(self):
        comments = [
            "You, sir, are my hero. Any chance you remember what page that's on?",
            "This book was clearly the best I have ever read in my entire life. I would recommend it to anyone who loves reading.",
            "Verry surprising, I didn't expect that at all. I'm really happy to see that you're doing well. Keep going on, you're the best !",
            "How come you're so good at this ? I'm really impressed by your work. Keep going on, you're the best !",
            "I spent a lot of time on this project, and I'm really happy to see that you like it. Keep going on, you're the best !",
            "It was not a good book. I would not recommend it to anyone.",
        ]

        for comment in comments:
            # comment checking
            input_str = self.vectorizer(comment)
            results = self.model.predict(np.expand_dims(input_str, 0))[0]
            # Convert from float32 to float64 pour la sérialisation JSON

            results = results.astype(np.float64)
            self.assertTrue(results[0] < 0.5)

    def test_comment_should_not_pass(self):
        """/!\ Please be counscious that the following comments are really offensive and racist.
        the test is here to check that the model is able to detect them as offensive. /!\ """

        comments = [
            "FUCK YOUR FILTHY MOTHER IN THE ASS, DRY!",
            "If you are anti-semitian, than shave your head bald and go to the skinhead meetings!",
            "You should do something nice for yourself, maybe go grab a couple of Horny Goat Weeds from your local convenience store and jack off for a little longer than three minutes tonight.",
            "First and last warning, you fucking gay - I won't appreciate if any more nazi shwain would write in my page! I don't wish to talk to you anymore!",
            "Don't look, come or think of comming back! Tosser.",
            "an exclusive group of some WP TALIBANS...who are good at destroying, self-appointed purist who GANG UP any one who asks them questions abt their ANTI-SOCIAL and DESTRUCTIVE (non)-contribution at WP?",
            "COCKSUCKER BEFORE YOU PISS AROUND ON MY WORK",
        ]

        for comment in comments:
            # comment checking
            input_str = self.vectorizer(comment)
            results = self.model.predict(np.expand_dims(input_str, 0))[0]
            # Convert from float32 to float64 pour la sérialisation JSON

            results = results.astype(np.float64)
            self.assertTrue(results[0] >= 0.5)
