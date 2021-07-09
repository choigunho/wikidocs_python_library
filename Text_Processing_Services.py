import textwrap
import re
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

    long_text = 'Life is too short, you need python. ' * 3

    def test_01_02(self):
        def wrap(long_text):
            return textwrap.wrap(long_text, width=70)

        self.assertEqual(
            ['Life is too short, you need python. Life is too short, you need', 'python. Life is too short, you need python.'],
            wrap(self.long_text)
        )

    data = """
    홍길동의 주민번호는 800905-1049118 입니다. 
    그리고 고길동의 주민번호는 700905-1059119 입니다. 
    그렇다면 누가 형님일까요?
    """

    def test_01_03(self):
        def reg():
            ex = re.compile('(\d{6})-\d{7}')
            return ex.sub('\g<1>-*******', self.data)

        print(reg())


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PrologLists)
    unittest.TextTestRunner(verbosity=2).run(suite)
