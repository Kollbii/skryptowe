from DeanerySystem.day import Day
from DeanerySystem.term import Term
# from DeanerySystem.timetable import Timetable1


class Lesson(object):
    
    def __init__(self, timetable ,term: Term, name: str, teacher_name: str, year: int, full_time :bool = True):
        self._timetable = timetable
        self._term = term
        self._name = name
        self._teacher_name = teacher_name
        self._year = year
        self._full_time = full_time

    #TODO Do better validation
    @property
    def timetable(self):
        return self._timetable

    @timetable.setter
    def setTimetable(self, timetable):
        self._timetable = timetable

    @property
    def term(self):
        return self._term

    @term.setter
    def setTerm(self, term):
        self._term = term

    @property
    def name(self):
        return self._name

    @name.setter
    def setName(self, name):
        self._name = name

    @property
    def teacherName(self):
        return self._teacher_name

    @teacherName.setter
    def setTeacherName(self, name):
        self._teacher_name = name

    @property
    def year(self):
        return self._year

    @year.setter
    def setYear(self, year):
        self._year = year

    @property
    def fullTime(self):
        return self._full_time

    @fullTime.setter
    def setFullTime(self, full_time):
        self._full_time = full_time

    def earlierDay(self):
        new_day = Day(7 if self._term._day.value - 1 == 0 else self._term._day.value - 1)
        new_term = Term(self._term._hour, self._term._minute, self._term._duration, new_day)

        if self._timetable.can_be_transferred_to(new_term, self._full_time):
            self._term._day = new_day
            return True
        else:
            # print("Przesunięcie w tył nie jest możliwe")
            return False


    def laterDay(self):
        new_day = Day(1 if self._term._day.value + 1 == 8 else self._term._day.value + 1)
        new_term = Term(self._term._hour, self._term._minute, self._term._duration, new_day)

        if self._timetable.can_be_transferred_to(new_term, self._full_time):
            self._term._day = new_day
            return True
        else:
            # print("Przesunięcie w przód nie jest możliwe")
            return False

    def earlierTime(self):
        hour_d = self._term._duration // 60
        min_d = self._term._duration % 60

        new_hour = self._term._hour - hour_d
        new_min = self._term._minute - min_d
        if new_min < 0:
            new_hour -= 1
            new_min = 60 + new_min
        
        new_term = Term(new_hour, new_min, self._term._duration, self._term._day)

        if self._timetable.can_be_transferred_to(new_term, self._full_time):
            self._term._hour = new_hour
            self._term._minute = new_min
            return True
        else:
            # print("Przesunięcie terminu do tyłu nie jest możliwe")
            return False        


    def laterTime(self):
        hour_d = self._term._duration // 60
        min_d = self._term._duration % 60

        new_hour = self._term._hour + hour_d
        new_min = self._term._minute + min_d
        if new_min > 60:
            new_hour += 1
            new_min = new_min - 60

        new_term = Term(new_hour, new_min, self._term._duration, self._term._day)

        if self._timetable.can_be_transferred_to(new_term, self._full_time):
            self._term._hour = new_hour
            self._term._minute = new_min
            return True
        else:
            # print("Przesunięcie terminu do przodu nie jest możliwe")
            return False        

    def __str__(self):
        #TODO Change printing
        return "{} ({})\n{} rok studiów {}\nProwadzący: {}".format(self._name, self._term, self._year, "stacjonarnych" if self._full_time else "niestacjonarnych", self._teacher_name)