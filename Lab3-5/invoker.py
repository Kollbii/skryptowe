from __future__ import annotations
import getopt, sys
from DeanerySystem.day import Day
from abc import ABC, abstractmethod
from DeanerySystem.term import Term
from DeanerySystem.break1 import Break
from DeanerySystem.lesson import Lesson
from DeanerySystem.teacher import Teacher
from DeanerySystem.base_term import BaseTerm
from DeanerySystem.timetable import Timetable1
from DeanerySystem.timetable2 import Timetable2


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class Action(Command):
    def __init__(self, action: str, table) -> None:
        self._action = action
        self._table = table

    def execute(self) -> None:
        print("Got executed")
        act = [str(self._action)]
        act = self._table.parse(act)
        self._table.perform(act)
        

class Invoker:
    _on_start = None

    def set_on_start(self, action, table):
        self._on_start = Action(action, table)

    def do_actions(self) -> None:
        if isinstance(self._on_start, Action):
            self._on_start.execute()


if __name__ == "__main__":
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

    table1= Timetable1()
    table = Timetable2([b1,b2,b3,b4,b5,b7])

    tables=[table1, table]

    t1 = Teacher("Tadeusz", "Wokulski")
    t2 = Teacher("Kamila", "Goste")
    t3 = Teacher("Tadeusz", "Wokulski")

    actions = ["t+", "t-", "t+", "d-"]
    act = table.parse(actions)

    lesson1 = Lesson(table, term1, "Algebra", t1, 2)
    lesson2 = Lesson(table, term2, "Sledcza", t1, 3)
    lesson3 = Lesson(table, term3, "WF", t2, 2, False)
    lesson4 = Lesson(table, term4, "Skryptowe", t2, 2)
    lesson6 = Lesson(table, term5, "InnePrzed", t2, 1, False)

    table.put(lesson1)
    table.put(lesson2)
    table.put(lesson3)
    table.put(lesson4)
    table.put(lesson6)

    table1.put(lesson1)
    table1.put(lesson2)
    table1.put(lesson6)

    # python invoker.py --table=1 --op=d+
    try:
        opts, args = getopt.getopt(sys.argv[1:], "to", ["table=", "opt="])
    except getopt.GetoptError:
        sys.exit(1)

    #Table number
    if tables[int(opts[0][1])]:
        work_table=tables[int(opts[0][1])]
        action=opts[1][1]

        print(work_table)

        inv = Invoker()
        inv.set_on_start(action, work_table)
        inv.do_actions()

        print(work_table)
