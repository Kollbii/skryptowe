from DeanerySystem.term import Term
from DeanerySystem.base_term import BaseTerm
from DeanerySystem.day import Day
from DeanerySystem.lesson import Lesson
from DeanerySystem.teacher import Teacher
from DeanerySystem.break1 import Break
from DeanerySystem.timetable2 import Timetable2

term1 = Term(8, 0, 90, Day.TUE)
term2 = Term(9, 35, 90, Day.WED)
term3 = Term(17, 20, 110, Day.FRI)
term4 = Term(9, 35, 90, Day.FRI)
term5 = Term(17, 20, 120, Day.SAT)


b1 = Break(BaseTerm(9, 30, 5))
b2 = Break(BaseTerm(11, 5, 10))
b3 = Break(BaseTerm(12, 45, 5))
b4 = Break(BaseTerm(14, 20, 20))
b5 = Break(BaseTerm(16, 10, 5))
b7 = Break(BaseTerm(19, 20, 10))

btable = Timetable2([b1,b2,b3,b4,b5,b7])

t1 = Teacher("Tadeusz", "Wokulski")
t2 = Teacher("Kamila", "Goste")
t3 = Teacher("Tadeusz", "Wokulski")

# actions = ["d-", "t-", "t+", "d+", "kods-"]   #Works well
actions = ["t+", "t-", "t+", "d-"]
act = btable.parse(actions)

lesson1 = Lesson(btable, term1, "Algebra", t1, 2)
lesson2 = Lesson(btable, term2, "Sledcza", t1, 3)
lesson3 = Lesson(btable, term3, "WF", t2, 2, False)
lesson4 = Lesson(btable, term4, "Skryptowe", t2, 2)
lesson5 = Lesson(btable, term4, "Skryptowe", t2, 2)

btable.put(lesson1)
btable.put(lesson2)
btable.put(lesson3)
btable.put(lesson4)
# btable.put(lesson5)   # Returns Exception


print(btable)
btable.perform(act)
print(btable)
lesson3.setTerm= Term(19, 20, 90, Day.FRI)
lesson3.earlierTime()
