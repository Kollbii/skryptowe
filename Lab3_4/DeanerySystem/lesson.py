from DeanerySystem.day import Day
from DeanerySystem.term import Term

class Lesson(object):
    def __init__(self, term: Term, name: str, teacher_name: str, year: int, full_time :bool = True):
        self.term = term
        self.name = name
        self.teacher_name = teacher_name
        self.year = year
        self.full_time = full_time

    def checkBoundary(self, new_day):
        if self.full_time and new_day.value in [1,2,3,4]:
            if self.term.hour >= 8 and self.term.hour <= 20:
                return True
        elif self.full_time and new_day.value in [5]:
            if self.term.hour >= 8 and self.term.hour <= 17:
                return True
        elif not self.full_time and new_day.value in [5]:
            if self.term.hour >= 17 and self.term.hour <= 20:
                return True
        elif not self.full_time and new_day.value in [6,7]:
            if self.term.hour >= 8 and self.term.hour <= 20:
                return True
        else:
            return False

    def checkDurationBoundary(self, new_hour, new_min):
        if self.full_time and self.term._day.value in [1,2,3,4]:
            if new_hour >= 8 and new_hour <=20:
                return True
        elif self.full_time and self.term._day.value in [5]:
            if new_hour >= 8 and new_hour <= 17:
                return True
        elif not self.full_time and self.term._day.value in [5]:
            if new_hour >= 17 and new_hour <= 20:
                return True
        elif not self.full_time and self.term._day.value in [6,7]:
            if new_hour >= 8 and new_hour <= 20:
                return True
        else:
            return False


    def earlierDay(self):
        new_day = Day(7 if self.term._day.value - 1 == 0 else self.term._day.value - 1)

        if self.checkBoundary(new_day):
            self.term._day = new_day
            return True
        else:
            # print("Przesunięcie w tył nie jest możliwe")
            return False


    def laterDay(self):
        new_day = Day(1 if self.term._day.value + 1 == 8 else self.term._day.value + 1)

        if self.checkBoundary(new_day):
            self.term._day = new_day
            return True
        else:
            # print("Przesunięcie w przód nie jest możliwe")
            return False

    def earlierTime(self):
        hour_d = self.term.duration // 60
        min_d = self.term.duration % 60

        new_hour = self.term.hour - hour_d
        new_min = self.term.minute - min_d
        if new_min < 0:
            new_hour -= 1
            new_min = 60 + new_min
        
        if self.checkDurationBoundary(new_hour, new_min):
            self.term.hour = new_hour
            self.term.minute = new_min
            return True
        else:
            # print("Przesunięcie terminu do tyłu nie jest możliwe")
            return False        


    def laterTime(self):
        hour_d = self.term.duration // 60
        min_d = self.term.duration % 60

        new_hour = self.term.hour + hour_d
        new_min = self.term.minute + min_d
        if new_min > 60:
            new_hour += 1
            new_min = 60 - new_min
        
        if self.checkDurationBoundary(new_hour, new_min):
            self.term.hour = new_hour
            self.term.minute = new_min
            return True
        else:
            # print("Przesunięcie terminu do tyłu nie jest możliwe")
            return False        

    def __str__(self):
        #TODO Change printing
        return "{} ({})\n{} rok studiów {}\nProwadzący: {}".format(self.name, self.term, self.year, "stacjonarnych" if self.full_time else "niestacjonarnych", self.teacher_name)