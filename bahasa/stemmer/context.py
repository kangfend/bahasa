from .utils import match_affix


class Context(object):
    def __init__(self, original_word, dictionary, visitor_provider):
        self.removals = []
        self.original_word = original_word
        self.current_word = self.original_word
        self.dictionary = dictionary
        self.result = self.original_word
        self.visitor_provider = visitor_provider
        self.is_stopped = False
        self.init_visitors()

    def init_visitors(self):
        self.visitors = self.visitor_provider.visitors
        self.suffix_visitors = self.visitor_provider.suffix_visitors
        self.prefix_visitors = self.visitor_provider.prefix_visitors

    def stop_process(self):
        self.is_stopped = True

    def add_removal(self, removal):
        self.removals.append(removal)

    def execute(self):
        # step 1 - 5
        self.start_stemming_process()

        # step 6
        if self.current_word in self.dictionary:
            self.result = self.current_word
        else:
            self.result = self.original_word

    def precedence(self, word):
        """
        Confix Stripping Rule Precedence Adjustment Specification.
        Asian J. (2007) "Effective Techniques for Indonesian Text Retrieval"
        Page 78-79.
        @link   http://researchbank.rmit.edu.au/eserv/rmit:6312/Asian.pdf
        """
        return True if any([
            match_affix(word, 'be', 'lah'),
            match_affix(word, 'be', 'an'),
            match_affix(word, 'me', 'i'),
            match_affix(word, 'di', 'i'),
            match_affix(word, 'pe', 'i'),
            match_affix(word, 'ter', 'i'),
        ]) else False

    def start_stemming_process(self):

        # step 1
        if self.current_word in self.dictionary:
            return
        self.accept_visitors(self.visitors)
        if self.current_word in self.dictionary:
            return

        # Confix Stripping
        # Try to remove prefix before suffix if the specification is met
        if self.precedence(self.original_word):
            # step 4, 5
            self.remove_prefixes()
            if self.current_word in self.dictionary:
                return

            # step 2, 3
            self.remove_suffixes()
            if self.current_word in self.dictionary:
                return
            else:
                # if the trial is failed, restore the original word
                # and continue to normal rule precedence (suffix first, prefix afterwards)
                self.current_word = self.original_word
                self.removals = []

        # step 2, 3
        self.remove_suffixes()
        if self.current_word in self.dictionary:
            return

        # step 4, 5
        self.remove_prefixes()
        if self.current_word in self.dictionary:
            return

        # ECS loop pengembalian akhiran
        self.loop_pengembalian_akhiran()

    def remove_prefixes(self):
        for i in range(3):
            self.accept_prefix_visitors(self.prefix_visitors)
            if self.current_word in self.dictionary:
                return

    def remove_suffixes(self):
        self.accept_visitors(self.suffix_visitors)

    def accept(self, visitor):
        visitor.visit(self)

    def accept_visitors(self, visitors):
        for visitor in visitors:
            self.accept(visitor)
            if self.current_word in self.dictionary:
                return self.current_word
            if self.is_stopped:
                return self.current_word

    def accept_prefix_visitors(self, visitors):
        removal_count = len(self.removals)
        for visitor in visitors:
            self.accept(visitor)
            if self.current_word in self.dictionary:
                return self.current_word
            if self.is_stopped:
                return self.current_word
            if len(self.removals) > removal_count:
                return

    def loop_pengembalian_akhiran(self):
        """ECS Loop Pengembalian Akhiran"""
        self.restore_prefix()

        removals = self.removals
        reversed_removals = reversed(removals)
        current_word = self.current_word

        for removal in reversed_removals:
            if not self.is_suffix_removal(removal):
                continue
            if removal.removed_part == 'kan':
                self.current_word = removal.result + 'k'

                # step 4,5
                self.remove_prefixes()
                if self.current_word in self.dictionary:
                    return
                self.current_word = removal.result + 'kan'
            else:
                self.current_word = removal.subject

            # step 4,5
            self.remove_prefixes()
            if self.current_word in self.dictionary:
                return

            self.removals = removals
            self.current_word = current_word

    def is_suffix_removal(self, removal):
        """Check wether the removed part is a suffix"""
        return removal.affix_type == 'DS' or \
            removal.affix_type == 'PP' or \
            removal.affix_type == 'P'

    def restore_prefix(self):
        """Restore prefix to proceed with ECS loop pengembalian akhiran"""
        for removal in self.removals:
            # return the word before precoding (the subject of first prefix removal)
            self.current_word = removal.subject
            break

        for removal in self.removals:
            if removal.affix_type == 'DP':
                self.removals.remove(removal)
