from typing import AnyStr
import skrypt
import unittest

class Test_TestSkrypt(unittest.TestCase):
    
    def test_word_numer(self):
        for answer in skrypt.extract("polskiText123more"):
            self.assertIn(answer, ["polskiText", 123, "more"])
    
    def test_only_word(self):
        for answer in skrypt.extract("dlugiteksttylkoze znakami i   spacjami"):
            self.assertEqual(answer, "dlugiteksttylkoze znakami i   spacjami")

    def test_only_nums(self):
        for answer in skrypt.extract("123 1355 -4359 321 0"):
            self.assertIn(answer, [123, 1355, -4359, 321, 0])


if __name__ == '__main__':
    unittest.main()