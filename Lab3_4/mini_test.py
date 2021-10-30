from DeanerySystem.term import Term
from DeanerySystem.day import Day
from DeanerySystem.lesson import Lesson
from DeanerySystem.timetable import Timetable1

lesson = Lesson(Term(9, 35, 90, Day.TUE), "Analiza", "Name Surrname", 2)
term1 = Term(9, 35, 90, Day.WED)
term2 = Term(9, 35, 90, Day.TUE)

lesson1 = Lesson(Term(9, 35, 90, Day.TUE), "Algebra", "Wokulski Tadeusz", 2)
lesson2 = Lesson(Term(17, 30, 110, Day.FRI), "Informatyka Sledcza", "Fabrowski Marcin", 3, False)
# print(lesson1)
# print(lesson2)
table = Timetable1()
actions = ["d+", "d-", "t-", "t+", "kods-"]
table.put(lesson1)
table.put(lesson2)
print(table)
actions = table.parse(actions)
print(actions)
print(table.busy(term1))
print(table.busy(term2))