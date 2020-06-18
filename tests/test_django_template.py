import unittest

from django_template import __version__


class TestDjangoTemplate(unittest.TestCase):
    def test_version(self):
        self.assertEqual(__version__, "0.1.0")
