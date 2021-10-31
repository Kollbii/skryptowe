from DeanerySystem.term import Term
from DeanerySystem.lesson import Lesson
from DeanerySystem.action import Action
from DeanerySystem.day import Day
from typing import List


class Timetable1(object):
    """ Class containing a set of operations to manage the timetable """
    def __init__(self):
        self._lessons = []
        
    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        if self.busy(term):
            print("Termin zajęty")
            return False
        
        if full_time and term.day.value in [1,2,3,4]:
            if term.hour >= 8 and term.hour <= 20:
                return True
        elif full_time and term.day.value in [5]:
            if term.hour >= 8 and term.hour <= 17:
                return True
        elif not full_time and term.day.value in [5]:
            if term.hour >= 17 and term.hour <= 20:
                return True
        elif not full_time and term.day.value in [6,7]:
            if term.hour >= 8 and term.hour <= 20:
                return True
        return False


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
        len_les = len(self._lessons)
        for (index, action) in enumerate(actions, start=0):
            if action == Action.DAY_EARLIER:
                self._lessons[index % len_les].earlierDay()
            elif action == Action.DAY_LATER:
                self._lessons[index % len_les].laterDay()
            elif action == Action.TIME_EARLIER:
                self._lessons[index % len_les].earlierTime()
            elif action == Action.TIME_LATER:
                self._lessons[index % len_les].laterTime()


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