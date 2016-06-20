from unittest import TestCase

from bahasa.stemmer.context import Context
from bahasa.stemmer.utils import load_dictionary
from bahasa.stemmer.visitor.provider import VisitorProvider


class ContextTest(TestCase):
    def test_context(self):
        visitor_provider = VisitorProvider()
        context = Context('berhalusinasi', load_dictionary(), visitor_provider)
        # This context result will return 'berhalusinasi'
        # because context has not been executed.
        self.assertNotEqual(context.result, 'halusinasi')
        context.execute()

        # This context will return 'halusinasi'
        # because context already executed.
        self.assertEqual(context.result, 'halusinasi')
