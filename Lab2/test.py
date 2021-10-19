import skrypt2
import unittest

class Test_TestSkrypt(unittest.TestCase):
    def test_word_numer(self):
        for answer in skrypt2.extract("polskiText123more"):
            self.assertIn(answer, ["polskiText", 123, "more"])
    
    def test_only_word(self):
        for answer in skrypt2.extract("DlugiTekstTylko znakami i   spacjami"):
            self.assertIn(answer, ["DlugiTekstTylko", "znakami", "i",   "spacjami"])

    def test_only_nums(self):
        for answer in skrypt2.extract("123 1355 -4359 321 0"):
            self.assertIn(answer, [123, 1355, -4359, 321, 0])

    def test_combine_all(self):
        for answer in skrypt2.extract("Full dis-99closure, Morty - it's not. Temporary superintell11igence."):
            self.assertIn(answer, [11,-99, "Full", "dis", "closure", "Morty", "it", "s", "not", "Temporary", "superintell", "igence"])

if __name__ == '__main__':
    unittest.main()