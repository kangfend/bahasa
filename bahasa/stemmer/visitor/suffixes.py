from ..removal import Removal
from ..utils import remove_suffix


class RemoveInflectionalParticle(object):
    """Remove Inflectional particle.
    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval".
    Page 60
    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    def visit(self, context):
        result = self.remove(context.current_word)
        if result != context.current_word:
            removed_part = remove_suffix(context.current_word, result)
            removal = Removal(self, context.current_word, result,
                              removed_part, 'P')
            context.add_removal(removal)
            context.current_word = result

    def remove(self, word):
        """Remove inflectional particle : lah|kah|tah|pun"""
        return remove_suffix(word, ['-lah', '-kah', '-tah', '-pun',
                                    'lah', 'kah', 'pun', 'tah'])


class RemoveDerivationalSuffix(object):
    """Remove Derivational Suffix.
    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval".
    Page 61
    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    def visit(self, context):
        result = self.remove(context.current_word)
        if result != context.current_word:
            removed_part = remove_suffix(context.current_word, result)
            removal = Removal(self, context.current_word, result,
                              removed_part, 'DS')
            context.add_removal(removal)
            context.current_word = result

    def remove(self, word):
        """Remove derivational suffix
        Original rule : i|kan|an
        Added the adopted foreign suffix rule : is|isme|isasi
        """
        return remove_suffix(word, ['is', 'isme', 'isasi', 'i', 'kan', 'an'])


class RemoveInflectionalPossessivePronoun(object):
    """Remove Inflectional Possessive Pronoun
    Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval".
    Page 60
    @link http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
    """

    def visit(self, context):
        result = self.remove(context.current_word)
        if result != context.current_word:
            removed_part = remove_suffix(context.current_word, result)
            removal = Removal(self, context.current_word, result,
                              removed_part, 'PP')
            context.add_removal(removal)
            context.current_word = result

    def remove(self, word):
        """Remove inflectional possessive pronoun : ku|mu|nya|-ku|-mu|-nya"""
        return remove_suffix(word, ['-ku', '-mu', '-nya', 'ku', 'mu', 'nya'])
