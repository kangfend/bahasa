import re

from .context import Context
from .utils import normalize_text, load_dictionary
from .visitor.provider import VisitorProvider


class Stemmer(object):
    def __init__(self, dictionary='default'):
        self.dictionary = load_dictionary(dictionary)
        self.visitor_provider = VisitorProvider()

    def stem(self, text):
        normalized_text = normalize_text(text)
        words = normalized_text.split()
        return " ".join([self.stem_word(word) for word in words])

    def stem_word(self, word):
        if self.is_plural(word):
            return self.stem_plural_word(word)
        return self.stem_singular_word(word)

    def is_plural(self, word):
        matches = re.match(r'^(.*)-(ku|mu|nya|lah|kah|tah|pun)$', word)
        return '-' in matches.group(1) if matches else '-' in word

    def stem_plural_word(self, plural):
        """Stem a plural word to its common stem form.
        Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval" page 76-77.
        @link   http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
        """
        plural = self.stem_singular_word(plural)
        if plural in self.dictionary:
            return plural

        matches = re.match(r'^(.*)-(.*)$', plural)
        if not matches:
            return plural
        words = list(matches.groups())

        # malaikat-malaikat-nya -> malaikat malaikat-nya
        suffix = words[1]
        suffixes = ['ku', 'mu', 'nya', 'lah', 'kah', 'tah', 'pun']
        matches = re.match(r'^(.*)-(.*)$', words[0])
        if suffix in suffixes and matches:
            words[0] = matches.group(1)
            words[1] = matches.group(2) + '-' + suffix

        # berbalas-balasan -> balas
        root_word_1 = self.stem_singular_word(words[0])
        root_word_2 = self.stem_singular_word(words[1])

        # meniru-nirukan -> tiru
        if words[1] not in self.dictionary and root_word_2 == words[1]:
            root_word_2 = self.stem_singular_word('me' + words[1])

        if root_word_1 == root_word_2:
            return root_word_1
        return plural

    def stem_singular_word(self, word):
        """Stem a singular word to its common stem form."""
        context = Context(word, self.dictionary, self.visitor_provider)
        context.execute()
        return context.result
