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