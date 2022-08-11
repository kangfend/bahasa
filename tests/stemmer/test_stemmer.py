from unittest import TestCase

from bahasa.stemmer import Stemmer


class StemmerTest(TestCase):
    def setUp(self):
        self.stemmer = Stemmer()

    def test_stem_word(self):
        self.assertEqual(self.stemmer.stem_word('menghasilkan'), 'hasil')
        self.assertEqual(self.stemmer.stem_word('ditandatangani'), 'tanda tangan')
        self.assertEqual(self.stemmer.stem_word('menyebarluaskan'), 'sebar luas')
        self.assertEqual(self.stemmer.stem_word('penghancurleburan'), 'hancur lebur')
        self.assertEqual(self.stemmer.stem_word('dilipatgandakan'), 'lipat ganda')
        self.assertEqual(self.stemmer.stem_word('pertanggungjawaban'), 'tanggung jawab')

    def test_stem_sentences(self):
        self.assertEqual(
            self.stemmer.stem('maka dokumen tersebut ditandatangani olehnya'), 
            'maka dokumen sebut tanda tangan oleh'
        )
        self.assertEqual(
            self.stemmer.stem('tiba-tiba disebarluaskanlah rahasia itu'),
            'tiba sebar luas rahasia itu'
        )
    
    def test_add_words(self):
        # Make sure word kasaha not exists in dictionary
        self.assertNotIn('kasaha', self.stemmer.dictionary)
        
        # Add one word
        self.stemmer.add_words('kasaha')
        self.assertIn('kasaha', self.stemmer.dictionary)

        # Make sure words kunaon & kumaha not exists in dictionary
        self.assertNotIn('kunaon', self.stemmer.dictionary)
        self.assertNotIn('kumaha', self.stemmer.dictionary)

        # Add multiple words
        self.stemmer.add_words('kunaon', 'kumaha')
        self.assertIn('kunaon', self.stemmer.dictionary)
        self.assertIn('kumaha', self.stemmer.dictionary)
    
    def test_remove_words(self):
        # Make sure word kasaha not exists in dictionary
        self.assertIn('ikan', self.stemmer.dictionary)

        # Remove one word
        self.stemmer.remove_words('ikan')
        self.assertNotIn('ikan', self.stemmer.dictionary)

        # Remove multiple words
        self.assertIn('batu', self.stemmer.dictionary)
        self.assertIn('bata', self.stemmer.dictionary)

        self.stemmer.remove_words('batu', 'bata')
        self.assertNotIn('batu', self.stemmer.dictionary)
        self.assertNotIn('bata', self.stemmer.dictionary)
