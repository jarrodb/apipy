
import sys, os.path
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..'))

from unittest import TestCase


class ApipyTestCase(TestCase):

    def _create_test_records(self):
        self._new_fixtures = [
            ]

    def setUp(self):
        super(ApipyTestCase, self).setUp()

