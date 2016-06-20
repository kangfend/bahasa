from ..removal import Removal
from ..utils import remove_prefix


class RemovePlainPrefix(object):
    def visit(self, context):
        result = self.remove(context.current_word)
        if result != context.current_word:
            removed_part = remove_prefix(context.current_word, result)
            removal = Removal(self, context.current_word, result,
                              removed_part, 'DP')
            context.add_removal(removal)
            context.current_word = result

    def remove(self, word):
        return remove_prefix(word, ['di', 'ke', 'se'])


class AbstractDisambiguatePrefixRule(object):
    """description of class"""

    def __init__(self):
        self.disambiguators = []

    def visit(self, context):
        result = None

        for disambiguator in self.disambiguators:
            result = disambiguator.disambiguate(context.current_word)
            if result in context.dictionary:
                break

        if not result:
            return

        removed_part = remove_prefix(context.current_word, result)
        removal = Removal(self, context.current_word, result, removed_part, 'DP')
        context.add_removal(removal)
        context.current_word = result

    def add_disambiguators(self, disambiguators):
        for disambiguator in disambiguators:
            self.add_disambiguator(disambiguator)

    def add_disambiguator(self, disambiguator):
        self.disambiguators.append(disambiguator)


class PrefixDisambiguator(AbstractDisambiguatePrefixRule):
    """description of class"""

    def __init__(self, disambiguators):
        super(PrefixDisambiguator, self).__init__()
        self.add_disambiguators(disambiguators)
