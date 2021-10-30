from DeanerySystem.term import Term
from DeanerySystem.day import Day
from DeanerySystem.lesson import Lesson

lesson = Lesson(Term(9, 35, 90, Day.TUE), "Analiza", "Name Surrname", 2)

lesson1 = Lesson(Term(9, 35, 90, Day.TUE), "Algebra", "Wokulski Tadeusz", 2)
lesson2 = Lesson(Term(17, 30, 110, Day.FRI), "Informatyka Sledcza", "Fabrowski Marcin", 3, False)
print(lesson1)
print(lesson2)
