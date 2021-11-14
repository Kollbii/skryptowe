from typing import List
from DeanerySystem.term import Term
from DeanerySystem.lesson import Lesson
from DeanerySystem.action import Action


class BaseTimetable(object):
    """ Class containing a set of operations to manage the timetable """
    def __init__(self):
        self._lessons = {}

    @property
    def lessons(self):
        return self._lessons
    
    @lessons.setter
    def setLessons(self, lesson):
        self._lessons[lesson.term] = lesson

    def busy(self, term: Term) -> bool:
        for le in list(self._lessons.values()):
            if le.term == term:
                return True
        return False

    def put(self, lesson: Lesson) -> bool:
        if type(lesson) == Lesson:
            if self.busy(lesson.term):
                raise ValueError("Term is busy!")
            self._lessons[lesson.term.__str__()] = lesson
            return True
        return False

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
            else:
                raise ValueError("Translation `" + opt + "` is incorrect.")
        return A

    def perform(self, actions: List[Action]):
        len_les = len(self._lessons)
        for (index, action) in enumerate(actions, start=0):
            if action == Action.DAY_EARLIER:
                list(self._lessons.values())[index % len_les].earlierDay()
            elif action == Action.DAY_LATER:
                list(self._lessons.values())[index % len_les].laterDay()
            elif action == Action.TIME_EARLIER:
                list(self._lessons.values())[index % len_les].earlierTime()
            elif action == Action.TIME_LATER:
                list(self._lessons.values())[index % len_les].laterTime()

    def get(self, term: Term) -> Lesson:
        for lesson in list(self._lessons.values()):
            if lesson.term == term:
                return lesson
        return None

    def getTotalHours(self, teacher):
        m_dur = 0
        h_dur = 0
        for lesson in list(self._lessons.values()):
            if lesson.teacher == teacher:
                h_dur += lesson.term.duration // 45 
                m_dur += lesson.term.duration % 45
        return h_dur*45 + m_dur
