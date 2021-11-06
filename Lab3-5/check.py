from DeanerySystem.term import Term
from DeanerySystem.day import Day
from DeanerySystem.lesson import Lesson
from DeanerySystem.timetable import Timetable1
from DeanerySystem.teacher import Teacher
from DeanerySystem.break1 import Break

term1 = Term(8, 0, 90, Day.TUE)
term2 = Term(9, 35, 90, Day.WED)
term3 = Term(17, 20, 110, Day.FRI)
term4 = Term(9, 35, 90, Day.FRI)
b1 = Break(Term(9, 30, 5))
b2 = Break(Term(11, 5, 10))
b3 = Break(Term(12, 45, 5))
b4 = Break(Term(14, 20, 20))

table = Timetable1()

t1 = Teacher("Tadeusz", "Wokulski")
t2 = Teacher("Kamila", "Goste")
t3 = Teacher("Tadeusz", "Wokulski")

lesson1 = Lesson(table, term1, "Algebra", t1, 2)
lesson2 = Lesson(table, term2, "Sledcza", t1, 3)
lesson3 = Lesson(table, term3, "WF", t2, 2, False)
lesson4 = Lesson(table, term4, "Skryptowe", t2, 2)

table.put(lesson1)
table.put(lesson2)
table.put(lesson3)
table.put(lesson4)

print(table)