from DeanerySystem.term import Term
from DeanerySystem.base_timetable import BaseTimetable
from DeanerySystem.break1 import Break
from typing import List


class Timetable2(BaseTimetable):
    def __init__(self, breaks: List[Break]):
        super().__init__()
        self._breaks = breaks

    @property
    def breaks(self):
        return self._breaks
    
    @breaks.setter
    def setBreaks(self, value):
        self._breaks.append(value)
        
    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        print("Implement can be transfered to breaks")

    def __str__(self):
        tabl = f'{"": <12}{"Poniedziałek": <12}{"*Wtorek": <12}{"*Środa": <12}{"*Czwartek": <12}{"*Piątek": <12}{"*Sobota": <12}{"*Niedziela": <12}\n'      
        tabl += f'{"": <12}{"*"*85}\n'
        
        times = []
        for lesson in self._lessons:
            times.append(lesson.term)
        for br in self._breaks:
            times.append(br)
        print(times)
        times = sorted(times, key=lambda x: x.hour or x.minute)
        print(times)
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