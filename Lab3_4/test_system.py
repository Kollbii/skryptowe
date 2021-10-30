import unittest
from DeanerySystem import Day
from DeanerySystem import Term
from DeanerySystem import Lesson


class Test_DSystem(unittest.TestCase):
    def setUp(self):
        global term1, term2, term3, lesson1, lesson2
        term1 = Term(9, 45, 90, Day.TUE)
        term2 = Term(11, 15, 30, Day.WED)
        term3 = Term(11, 15, 90,Day.TUE)
        lesson1 = Lesson(Term(9, 35, 90, Day.TUE), "Algebra", "Wokulski Tadeusz", 2)
        lesson2 = Lesson(Term(17, 30, 110, Day.FRI), "Informatyka Sledcza", "Fabrowski Marcin", 3, False)

    def test_earlier(self):
        self.assertEqual(term1.earlierThan(term2), True)
        self.assertEqual(term2.earlierThan(term1), False)

    def test_later(self):
        self.assertEqual(not term1.earlierThan(term2), False)
        self.assertEqual(not term2.earlierThan(term1), True)
        
    def test_equal(self):
        self.assertEqual(term1.equals(term2), False)
        self.assertEqual(term1.equals(term3), False)

    def test_represent(self):
        self.assertEqual(term1.__str__(), "Wtorek 9:45 [90]")
        self.assertEqual(term2.__str__(), "Środa 11:15 [30]")
        self.assertEqual(term3.__str__(), "Wtorek 11:15 [90]")

    def test_set_term(self):
        self.assertEqual(term1.setTerm("27 X 2021 8:10 - 27 X 2021 8:30"), True)
        self.assertEqual(term2.setTerm("27 X 2021 8:30 - 28 X 2021 8:00"), True)
        self.assertEqual(term3.setTerm("28 X 2021 12:20 - 28 X 2021 14:20"), True)

    #Unit test for lab 4
    def test_lesson_represent(self):
        self.assertEqual(lesson1.__str__(), "Algebra (Wtorek 9:35 [90])\n2 rok studiów stacjonarnych\nProwadzący: Wokulski Tadeusz")
        self.assertEqual(lesson2.__str__(), "Informatyka Sledcza (Piątek 17:30 [110])\n3 rok studiów niestacjonarnych\nProwadzący: Fabrowski Marcin")

    def test_earlier_day(self):
        self.assertEqual(lesson1.earlierDay(), True)
        self.assertEqual(lesson2.earlierDay(), False)

    def test_later_day(self):
        self.assertEqual(lesson1.laterDay(), True)
        self.assertEqual(lesson2.laterDay(), True)

    def test_earlier_time(self):
        self.assertEqual(lesson1.earlierTime(), True)
        self.assertEqual(lesson2.earlierTime(), False)

    def test_later_time(self):
        self.assertEqual(lesson1.laterTime(), True)
        self.assertEqual(lesson2.laterTime(), True)

    def test_term_operators(self):
        self.assertEqual(term1 < term3 , True)
        self.assertEqual(term1 <= term3, True)
        self.assertEqual(term1 > term3, False)
        self.assertEqual(term1 >= term3, False)
        self.assertEqual(term2 == term2, True)
        self.assertEqual(term2 == term3, False)
        self.assertEqual(term3 - term1, Term(9, 45, 180, Day.TUE))