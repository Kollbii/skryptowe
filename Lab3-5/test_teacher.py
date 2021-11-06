import unittest
from DeanerySystem.term import Term
from DeanerySystem.day import Day
from DeanerySystem.lesson import Lesson
from DeanerySystem.timetable import Timetable1
from DeanerySystem.teacher import Teacher


class Test_TestDay(unittest.TestCase):
    def setUp(self):
        global term1, term2, term3, table, t1, t2, lesson1, lesson2, lesson3, t3
        term1 = Term(9, 45, 90, Day.TUE)
        term2 = Term(11, 15, 90, Day.WED)
        term3 = Term(17, 30, 110, Day.FRI)

        table = Timetable1()

        t1 = Teacher("Tadeusz", "Wokulski")
        t2 = Teacher("Kamila", "Goste")
        t3 = Teacher("Tadeusz", "Wokulski")

        lesson1 = Lesson(table, term1, "Algebra", t1, 2)
        lesson2 = Lesson(table, term2, "Sledcza", t1, 3)
        lesson3 = Lesson(table, term3, "WF", t2, 2,False)

        table.put(lesson1)
        table.put(lesson2)
        table.put(lesson3)

    def test_lesson_add(self):
        self.assertEqual(lesson1 + t2, True)
        self.assertEqual(lesson1 + t2, False)

    def test_lesson_sub(self):
        self.assertEqual(lesson2 - t1, True)
        self.assertEqual(lesson3 - t1, False)
    
    def test_different_techers_with_same_name(self):
        self.assertEqual(t1 == t3, False)
        self.assertEqual(t1 == t1, True)


if __name__ == '__main__':
    unittest.main()