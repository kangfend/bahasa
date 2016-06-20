class Removal(object):
    def __init__(self, visitor, subject, result, removed_part, affix_type):
        self.visitor = visitor
        self.subject = subject
        self.result = result
        self.removed_part = removed_part
        self.affix_type = affix_type
