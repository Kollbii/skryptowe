from DeanerySystem.day import Day
from DeanerySystem.term import Term

class Lesson(object):
    def __init__(self, term: Term, name: str, teacher_name: str, year: int, full_time :bool = True):
        self._term = term
        self._name = name
        self._teacher_name = teacher_name
        self._year = year
        self._full_time = full_time

    #TODO Do better validation
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


    def checkBoundary(self, new_day):
        if self._full_time and new_day.value in [1,2,3,4]:
            if self._term._hour >= 8 and self._term._hour <= 20:
                return True
        elif self._full_time and new_day.value in [5]:
            if self._term._hour >= 8 and self._term._hour <= 17:
                return True
        elif not self._full_time and new_day.value in [5]:
            if self._term._hour >= 17 and self._term._hour <= 20:
                return True
        elif not self._full_time and new_day.value in [6,7]:
            if self._term._hour >= 8 and self._term._hour <= 20:
                return True
        else:
            return False

    def checkDurationBoundary(self, new_hour, new_min):
        if self._full_time and self._term._day.value in [1,2,3,4]:
            if new_hour >= 8 and new_hour <=20:
                return True
        elif self._full_time and self._term._day.value in [5]:
            if new_hour >= 8 and new_hour <= 17:
                return True
        elif not self._full_time and self._term._day.value in [5]:
            if new_hour >= 17 and new_hour <= 20:
                return True
        elif not self._full_time and self._term._day.value in [6,7]:
            if new_hour >= 8 and new_hour <= 20:
                return True
        else:
            return False


    def earlierDay(self):
        new_day = Day(7 if self._term._day.value - 1 == 0 else self._term._day.value - 1)
        new_term = Term(self._term._hour, self._term._minute, self._term._duration, new_day)


        if self.checkBoundary(new_day):
            self._term._day = new_day
            return True
        else:
            # print("Przesunięcie w tył nie jest możliwe")
            return False


    def laterDay(self):
        new_day = Day(1 if self._term._day.value + 1 == 8 else self._term._day.value + 1)

        if self.checkBoundary(new_day):
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
        
        if self.checkDurationBoundary(new_hour, new_min):
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
            new_min = 60 - new_min
        
        if self.checkDurationBoundary(new_hour, new_min):
            self._term._hour = new_hour
            self._term._minute = new_min
            return True
        else:
            # print("Przesunięcie terminu do tyłu nie jest możliwe")
            return False        

    def __str__(self):
        #TODO Change printing
        return "{} ({})\n{} rok studiów {}\nProwadzący: {}".format(self._name, self._term, self._year, "stacjonarnych" if self._full_time else "niestacjonarnych", self._teacher_name)