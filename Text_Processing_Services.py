import random, itertools
import unittest


class PrologLists(unittest.TestCase):
    def test_1_1(self):
        def last(li):
            return li[-1]

        self.assertEquals(5, last([1, 2, 3, 4, 5]))
        self.assertEquals(-5, last([-1, -2, -3, -4, -5]))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PrologLists)
    unittest.TextTestRunner(verbosity=2).run(suite)