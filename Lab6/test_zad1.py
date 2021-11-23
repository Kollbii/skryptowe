import unittest
from zad1 import Operacje


class Test_Zad1(unittest.TestCase):
    def setUp(self):
        global op
        op=Operacje()
        
    def test_operation_sum(self):
        self.assertEqual(op.suma(1,2,3), 4)
        self.assertEqual(op.suma(1,2), 5)
        self.assertEqual(op.suma(1), None)

    def test_operation_error(self):
        with self.assertRaises(TypeError):
            op.suma()

    def test_operation_roznica(self):
        self.assertEqual(op.roznica(2,1), 4)
        self.assertEqual(op.roznica(2), 5)
        self.assertEqual(op.roznica(), 6)

    def test_change_sum(self):
        op['suma']=[1,2]
        self.assertEqual(op.suma(1), None)
        self.assertEqual(op.suma(1, 1), 2)
        self.assertEqual(op.suma(1, 1, 1), 1)

    def test_change_roznica(self):
        op['roznica']=[1,2,3]
        self.assertEqual(op.roznica(), 3)
        self.assertEqual(op.roznica(1), 2)
        self.assertEqual(op.roznica(1, 1), 1)

if __name__ == "__main__":
    unittest.main()