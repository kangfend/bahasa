from unittest import TestCase

from bahasa.stemmer.utils import (
    match_affix, normalize_text, remove_prefix, remove_suffix,
    load_dictionary
)


class UtilityTest(TestCase):
    def test_match_affix(self):
        # This should return True
        # The word 'terlupakan' contains prefix 'ter'
        # and suffix 'kan'
        self.assertTrue(match_affix('terlupakan', 'ter', 'kan'))

        self.assertTrue(match_affix('lupakan', suffix='kan'))
        self.assertTrue(match_affix('berharga', prefix='ber'))

        # This should return False
        # The word 'terdampar' doesn't contains prefix 'per'
        self.assertFalse(match_affix('terdampar', 'per'))

    def test_normalize_text(self):
        self.assertEqual(normalize_text('siapa namamu?'), 'siapa namamu')
        self.assertEqual(normalize_text('Jangan buang sampah sembarangan!'),
                         'jangan buang sampah sembarangan')

    def test_remove_prefix(self):
        self.assertEqual(remove_prefix('bercanda', ['ber']), 'canda')
        self.assertEqual(remove_prefix('dilanda', 'di'), 'landa')

    def test_remove_suffix(self):
        self.assertEqual(remove_suffix('buanglah', ['lah']), 'buang')
        self.assertEqual(remove_suffix('biarkan', 'kan'), 'biar')

    def test_load_dictionary(self):
        data = set(['aba', 'rasa', 'cinta'])
        dictionary = load_dictionary(data)
        self.assertEqual(dictionary, data)
        self.assertTrue('aba' in dictionary)
        self.assertTrue('rasa' in dictionary)
        self.assertTrue('cinta' in dictionary)
        self.assertFalse('dosa' in dictionary)
