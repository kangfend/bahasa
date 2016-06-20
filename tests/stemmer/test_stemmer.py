from unittest import TestCase

from bahasa.stemmer import Stemmer


class StemmerTest(TestCase):
    def setUp(self):
        self.stemmer = Stemmer()

    def test_stem_word(self):
        self.assertEqual(self.stemmer.stem_word('menghasilkan'), 'hasil')
