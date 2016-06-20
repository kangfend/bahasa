from . import DontStemShortWord
from ..disambiguator import prefixes

from .prefixes import (RemovePlainPrefix, PrefixDisambiguator)
from .suffixes import (RemoveInflectionalParticle, RemoveDerivationalSuffix,
                       RemoveInflectionalPossessivePronoun)


class VisitorProvider(object):
    def __init__(self):
        self.visitors = [
            DontStemShortWord()
        ]
        self.suffix_visitors = [
            RemoveInflectionalParticle(),
            RemoveInflectionalPossessivePronoun(),
            RemoveDerivationalSuffix(),
        ]
        self.prefix_visitors = [
            RemovePlainPrefix(),
            PrefixDisambiguator([
                prefixes.Rule1a(),
                prefixes.Rule1b(),
            ]),
            PrefixDisambiguator([prefixes.Rule2()]),
            PrefixDisambiguator([prefixes.Rule3()]),
            PrefixDisambiguator([prefixes.Rule4()]),
            PrefixDisambiguator([prefixes.Rule5()]),
            PrefixDisambiguator([
                prefixes.Rule6a(),
                prefixes.Rule6b(),
            ]),
            PrefixDisambiguator([prefixes.Rule7()]),
            PrefixDisambiguator([prefixes.Rule8()]),
            PrefixDisambiguator([prefixes.Rule9()]),
            PrefixDisambiguator([prefixes.Rule10()]),
            PrefixDisambiguator([prefixes.Rule11()]),
            PrefixDisambiguator([prefixes.Rule12()]),
            PrefixDisambiguator([
                prefixes.Rule13a(),
                prefixes.Rule13b(),
            ]),
            PrefixDisambiguator([prefixes.Rule14()]),
            PrefixDisambiguator([
                prefixes.Rule15a(),
                prefixes.Rule15b(),
            ]),
            PrefixDisambiguator([prefixes.Rule16()]),
            PrefixDisambiguator([
                prefixes.Rule17a(),
                prefixes.Rule17b(),
                prefixes.Rule17c(),
                prefixes.Rule17d(),
            ]),
            PrefixDisambiguator([
                prefixes.Rule18a(),
                prefixes.Rule18b(),
            ]),
            PrefixDisambiguator([prefixes.Rule19()]),
            PrefixDisambiguator([prefixes.Rule20()]),
            PrefixDisambiguator([
                prefixes.Rule21a(),
                prefixes.Rule21b(),
            ]),
            PrefixDisambiguator([prefixes.Rule23()]),
            PrefixDisambiguator([prefixes.Rule24()]),
            PrefixDisambiguator([prefixes.Rule25()]),
            PrefixDisambiguator([
                prefixes.Rule26a(),
                prefixes.Rule26b(),
            ]),
            PrefixDisambiguator([prefixes.Rule27()]),
            PrefixDisambiguator([
                prefixes.Rule28a(),
                prefixes.Rule28b(),
            ]),
            PrefixDisambiguator([prefixes.Rule29()]),
            PrefixDisambiguator([
                prefixes.Rule30a(),
                prefixes.Rule30b(),
                prefixes.Rule30c(),
            ]),
            PrefixDisambiguator([
                prefixes.Rule31a(),
                prefixes.Rule31b(),
            ]),
            PrefixDisambiguator([prefixes.Rule32()]),
            PrefixDisambiguator([prefixes.Rule34()]),
            PrefixDisambiguator([prefixes.Rule35()]),
            PrefixDisambiguator([prefixes.Rule36()]),
            PrefixDisambiguator([
                prefixes.Rule37a(),
                prefixes.Rule37b(),
            ]),
            PrefixDisambiguator([
                prefixes.Rule38a(),
                prefixes.Rule38b(),
            ]),
            PrefixDisambiguator([
                prefixes.Rule39a(),
                prefixes.Rule39b(),
            ]),
            PrefixDisambiguator([
                prefixes.Rule40a(),
                prefixes.Rule40b(),
            ]),
            PrefixDisambiguator([prefixes.Rule41()]),
            PrefixDisambiguator([prefixes.Rule42()]),
        ]

    def get_visitors(self):
        return self.visitors

    def get_suffix_visitors(self):
        return self.suffix_visitors

    def get_prefix_visitors(self):
        return self.prefix_pisitors
