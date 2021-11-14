from DeanerySystem.term import Term
from DeanerySystem.base_timetable import BaseTimetable


class Timetable1(BaseTimetable):
    def __init__(self):
        super().__init__()

    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        if self.busy(term):
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

    def __str__(self):
        tabl = f'{"": <12}{"Poniedziałek": <12}{"*Wtorek": <12}{"*Środa": <12}{"*Czwartek": <12}{"*Piątek": <12}{"*Sobota": <12}{"*Niedziela": <12}\n'      
        tabl += f'{"": <12}{"*"*85}\n'
        
        times = []
        for lesson in list(self._lessons.values()):
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
                        to_display[i - count][day] = f'{"*"+lesson.name: <12}'
            else:
                count += 1

        for i in range(len(to_display) - count):
            for j in range(len(to_display[i])):
                tabl += f'{to_display[i][j]}'
            tabl += f'*\n{" ": <12}'
            tabl += f'{"*"*85}\n'

        return tabl