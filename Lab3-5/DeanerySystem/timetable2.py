from typing import List
from DeanerySystem.term import Term
from DeanerySystem.break1 import Break
from DeanerySystem.lesson import Lesson
from DeanerySystem.timetable import Timetable1


class Timetable2(Timetable1):
    skipBreaks: bool = True
    def __init__(self, breaks: List[Break]):
        super().__init__()
        self._breaks = breaks

    @property
    def breaks(self):
        return self._breaks
    
    @breaks.setter
    def setBreaks(self, value):
        self._breaks.append(value)
    
    def onBreak(self, term):
        for br in self._breaks:
            end_h_br, end_m_br = br.getEndTime()
            start_h_br, start_m_br = br.getStartTime()
            start_h_term, start_m_term = term.getStartTime()
            end_h_term, end_m_term = term.getEndTime()
            
            if (int(end_h_br), int(end_m_br)) > (int(start_h_term), int(start_m_term)):
                return True, br.duration

            if (int(end_h_term), int(end_m_term)) > (int(start_h_br), int(start_m_br)):
                return True, br.duration
        
        return False,

    def updateLessons(self, timetable):
        self._lessons = timetable.lessons

    #TODO
    # def busy(self, term: Term) -> bool:
    #     pass

    # def put(self, lesson: Lesson) -> bool:
    #     if type(lesson) == Lesson:
    #         for le in list(self._lessons.values()):
    #             if le.term == lesson.term:
    #                 raise ValueError("Term is busy!")

    #             #TODO Check if overlaps with breaks
    #             if 1:
    #                 pass
    #             print(lesson.term)

    #             return True
    #     return False

    def __str__(self):
        tabl = f'{"": <12}{"Poniedziałek": <12}{"*Wtorek": <12}{"*Środa": <12}{"*Czwartek": <12}{"*Piątek": <12}{"*Sobota": <12}{"*Niedziela": <12}\n'      
        tabl += f'{"": <12}{"*"*85}\n'
        
        times = []
        for lesson in list(self._lessons.values()):
            times.append(lesson.term)
        for br in self._breaks:
            times.append(br)
        times = sorted(times, key=lambda x: x.getUniqueStartingHours())

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

                if type(times[i]) == Break:
                    for j in range(7):
                        to_display[i-count][j+1] = f'{"-"*12}'
                
                if type(times[i]) == Term:
                    for lesson in list(self._lessons.values()):
                        if lesson.term.hour == times[i].hour and lesson.term.minute == times[i].minute and lesson.term.duration == times[i].duration:
                            day = lesson.term.day.value
                            to_display[i - count][day] = f'{"*"+lesson.name: <12}'
            else:
                count += 1

        for i in range(len(to_display) - count):
            for j in range(len(to_display[i])):
                tabl += f'{to_display[i][j]}'
            tabl += f'*\n{" ": <12}'
            tabl += f'{"*"*85}\n'

        return tabl