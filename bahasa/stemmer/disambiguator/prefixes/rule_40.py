import re


class Rule40a(object):
    """Disambiguate Prefix Rule 40a (CC infix rules)
    Rule 40a : CinV -> CinV
    """

    def disambiguate(self, word):
        """Disambiguate Prefix Rule 40a (CC infix rules)
        Rule 40a : CinV -> CinV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])(in[aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)


class Rule40b(object):
    """Disambiguate Prefix Rule 40b (CC infix rules)
    Rule 40b : CinV -> CV
    """

    def disambiguate(self, word):
        """Disambiguate Prefix Rule 40b (CC infix rules)
        Rule 40b : CinV -> CV
        """
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])in([aiueo])(.*)$', word)
        if matches:
            return matches.group(1) + matches.group(2) + matches.group(3)
