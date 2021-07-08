import random, itertools
import textwrap
import unittest

'''
https://wikidocs.net/book/5445
'''


class PrologLists(unittest.TestCase):
    def test_01_01(self):
        def shorten(text):
            return textwrap.shorten(text, width=15, placeholder="...")

        self.assertEqual("Life is too...", shorten("Life is too short, you need python"))
        self.assertEqual("Hello World", shorten("Hello World"))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PrologLists)
    unittest.TextTestRunner(verbosity=2).run(suite)
