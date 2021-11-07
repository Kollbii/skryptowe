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
