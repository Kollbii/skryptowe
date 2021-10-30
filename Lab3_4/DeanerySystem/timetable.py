from DeanerySystem.term import Term
from DeanerySystem.lesson import Lesson
from DeanerySystem.day import Day
from DeanerySystem.action import Action
from typing import List


class Timetable1(object):
    """ Class containing a set of operations to manage the timetable """
    def __init__(self):
        self._lessons = []
        
    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:

        pass


    def busy(self, term: Term) -> bool:
        for lesson in self._lessons:
            if lesson.term == term:
                return True
            else:
                return False


    def put(self, lesson: Lesson) -> bool:
        True if self._lessons.append(lesson) else False

    def parse(self, actions: List[str]) -> List[Action]:
        A = []
        for opt in actions:
            if opt == "d-":
                A.append(Action.DAY_EARLIER)
            elif opt == "d+":
                A.append(Action.DAY_LATER)
            elif opt == "t-":
                A.append(Action.TIME_EARLIER)
            elif opt == "t+":
                A.append(Action.TIME_LATER)
        return A


    def perform(self, actions: List[Action]):
        """
        Transfer the lessons included in the timetable as described in the list of actions. N-th action should be sent the n-th lesson in the timetable.

        Parameters
        ----------
        actions : List[Action]
        Actions to be performed
        """

        pass

    def get(self, term: Term) -> Lesson:
        for lesson in self._lessons:
            if lesson.term == term:
                return lesson
        return None

    def __str__(self):
        string = ""
        for lesson in self._lessons:
            string += ''.join(str(lesson.name)+" --> "+str(lesson.term) + "\n")
        return string