import unittest
from DeanerySystem.term import Term
from DeanerySystem.base_term import BaseTerm
from DeanerySystem.day import Day
from DeanerySystem.lesson import Lesson
from DeanerySystem.teacher import Teacher
from DeanerySystem.break1 import Break
from DeanerySystem.timetable2 import Timetable2


class Test_DSystem(unittest.TestCase):
    def setUp(self):
        global term1, term2, term3, term4, term5, lesson1, lesson2, lesson3, lesson4, lesson5, lesson6
        global b1, b2, b3, b4, t1, t2, t3, act, actions, table
                
        term1 = Term(8, 0, 90, Day.TUE)
        term2 = Term(9, 35, 90, Day.WED)
        term3 = Term(17, 20, 110, Day.FRI)
        term4 = Term(9, 35, 90, Day.FRI)
        term5 = Term(17, 20, 110, Day.SAT)


        b1 = Break(BaseTerm(9, 30, 5))
        b2 = Break(BaseTerm(11, 5, 10))
        # b3 = Break(BaseTerm(12, 45, 5))
        # b4 = Break(BaseTerm(14, 20, 20))

        table = Timetable2([b1,b2])

        t1 = Teacher("Tadeusz", "Wokulski")
        t2 = Teacher("Kamila", "Goste")
        t3 = Teacher("Tadeusz", "Wokulski")

        actions = ["t+", "t-", "t+", "d-"]
        act = table.parse(actions)

        lesson1 = Lesson(table, term1, "Algebra", t1, 2)
        lesson2 = Lesson(table, term2, "Sledcza", t1, 3)
        lesson3 = Lesson(table, term3, "WF", t2, 2, False)
        lesson4 = Lesson(table, term4, "Skryptowe", t2, 2)
        lesson5 = Lesson(table, term4, "Skryptowe", t2, 2)
        lesson6 = Lesson(table, term5, "InnePrzed", t2, 2, False)

        table.put(lesson1)
        table.put(lesson2)
        table.put(lesson3)
        table.put(lesson4)
        table.put(lesson6)

        # table.updateLessons(table)
        # print(table)

    '''
    Wszystkie funkcje mają zapewniać poprawne działanie funkcji earlier*() oraz later*()
    Sprawdzam skrajne przypadki przesuwania zajęć. 
    '''

    def test_later_in_total(self):
        self.assertTrue(lesson1.laterTime())
        self.assertTrue(lesson2.laterTime())
        self.assertTrue(lesson3.laterTime())
        self.assertTrue(lesson4.laterTime())

    def test_earlier_in_total(self):
        self.assertFalse(lesson1.earlierTime())
        self.assertTrue(lesson2.earlierTime())
        self.assertFalse(lesson3.earlierTime())
        self.assertTrue(lesson4.earlierTime())

    def test_later_day(self):
        self.assertFalse(lesson3.laterDay())

    def test_before_8am(self):
        self.assertTrue(lesson2.earlierTime())
        self.assertFalse(lesson2.earlierTime())

    def change_lesson3(self):
        global lesson3
        lesson3 = Lesson(table, Term(19, 20, 120, Day.FRI), "WF", t2, 2, False)

    def test_before_17(self):
        self.assertFalse(lesson3.earlierTime())
        self.change_lesson3()
        self.assertTrue(lesson3.earlierTime())
        self.assertFalse(lesson3.earlierDay())
        self.assertTrue(lesson3.laterDay())

    def test_raise_value_error_parse(self):
        global actions
        actions = ["t+", "t-", "t+", "d-", "kods-"]
        with self.assertRaises(ValueError):
            table.parse(actions)

    def test_raise_add_lesson_on_busy_term(self):
        with self.assertRaises(ValueError):
            table.put(lesson5)

    