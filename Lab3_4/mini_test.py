from DeanerySystem.term import Term
from DeanerySystem.day import Day
from DeanerySystem.lesson import Lesson
from DeanerySystem.timetable import Timetable1

term1 = Term(9, 35, 90, Day.WED)
term2 = Term(9, 35, 90, Day.TUE)
term3 = Term(17, 30, 110, Day.FRI)

table = Timetable1()

lesson1 = Lesson(table, term2, "Algebra", "Wokulski Tadeusz", 2)
lesson2 = Lesson(table, term3, "Informatyka Sledcza", "Fabrowski Marcin", 3, False)
# print(lesson1)
# lesson1.earlierDay()
# print("*"*20)
# print(lesson1)
# print("*"*20)
# print(lesson2)
# lesson2.laterTime()
# print("*"*20)
# print(lesson2)

actions = ["t-", "d-", "t+", "d-", "kods-"]
table.put(lesson1)
table.put(lesson2)
print(table)
actions = table.parse(actions)
print(actions)
print(table.busy(term1))
print(table.busy(term2))

table.perform(actions)