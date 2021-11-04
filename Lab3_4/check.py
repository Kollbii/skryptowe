from DeanerySystem.term import Term
from DeanerySystem.day import Day
from DeanerySystem.lesson import Lesson
from DeanerySystem.timetable import Timetable1

term1 = Term(9, 45, 90, Day.TUE)
term2 = Term(11, 15, 30, Day.WED)
term3 = Term(11, 15, 90, Day.TUE)
term4 = Term(17, 30, 110, Day.FRI)

table = Timetable1()
tables = 's'
print(type(tables) == Timetable1)
lesson1 = Lesson(tables, term1, "Algebra", "Wokulski Tadeusz", 2)
lesson2 = Lesson(table, term2, "Sledcza", "Fabrowski Marcin", 3)
lesson3 = Lesson(table, term4, "WF", "Stojkowski Goste", 2,False)

# print(table)

# print(lesson1)
# lesson1.earlierDay()
# print("*"*20)
# print(lesson1)
# print("*"*20)
# print(lesson2)
# lesson2.laterTime()
# print("*"*20)
# print(lesson2)
# print(lesson3)

table.put(lesson1)
table.put(lesson2)
table.put(lesson3)
print(table)

actions = ["t-", "d-", "t+", "d-", "kods-"]
actions = table.parse(actions)
# print(actions)

# print(table.busy(term1))
# print(table.busy(term2))

table.perform(actions)
print(table)