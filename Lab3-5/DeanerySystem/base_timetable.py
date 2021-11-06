from DeanerySystem.term import Term
from DeanerySystem.lesson import Lesson
from DeanerySystem.action import Action
from DeanerySystem.teacher import Teacher
from typing import List


class BaseTimetable(object):
    """ Class containing a set of operations to manage the timetable """
    def __init__(self):
        self._lessons = []

    def busy(self, term: Term) -> bool:
        #TODO nachodzace terminy
        for lesson in self._lessons:
            if lesson.term == term:
                return True
            if lesson.term.hour == term.hour and (lesson.term.minute >= term.minute):
                return True
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

    def getTotalHours(self, teacher):
        m_dur = 0
        h_dur = 0
        for lesson in self._lessons:
            if lesson.teacher == teacher:
                h_dur += lesson.term.duration // 45 
                m_dur += lesson.term.duration % 45
        return h_dur*45 + m_dur

    def __str__(self):
        tabl = f'{"": <12}{"Poniedziałek": <12}{"*Wtorek": <12}{"*Środa": <12}{"*Czwartek": <12}{"*Piątek": <12}{"*Sobota": <12}{"*Niedziela": <12}\n'      
        tabl += f'{"": <12}{"*"*85}\n'
        
        times = []
        for lesson in self._lessons:
            times.append(lesson.term)
        times = sorted(times, key=lambda x: x.hour or x.minute)

        to_display = [[f'{"*": <12}' for x in range(8)] for y in range(len(times))]

        prev_hour = []

        count = 0
        
        for i in range(len(times)):
            if [times[i].hour, times[i].minute, times[i].duration] != prev_hour:
                prev_hour = [times[i].hour, times[i].minute, times[i].duration]
                
                end_hour, end_min = times[i].getEndTime()
                start_hour, start_min = times[i].getStartTime()

                start = f'{start_hour}:{start_min}'
                end = f'{end_hour}:{end_min}'
                
                to_display[i-count][0] = f'{start+"-"+end: <12}'

                for lesson in self._lessons:
                    if lesson.term.hour == times[i].hour and lesson.term.minute == times[i].minute and lesson.term.duration == times[i].duration:
                        day = lesson.term.day.value
                        # Option with centering
                        
                        # to_display[i][day] = "*"
                        # to_display[i][day] += f'{lesson.name: ^12}'
                        
                        # Default
                        to_display[i - count][day] = f'{"*"+lesson.name: <12}'
            else:
                count += 1

        for i in range(len(to_display) - count):
            for j in range(len(to_display[i])):
                tabl += f'{to_display[i][j]}'
            tabl += f'*\n{" ": <12}'
            tabl += f'{"*"*85}\n'

        return tabl