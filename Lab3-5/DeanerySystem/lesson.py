from DeanerySystem.day import Day
from DeanerySystem.term import Term
from DeanerySystem.teacher import Teacher
from DeanerySystem.lesson_exception import LessonError

class Lesson(object):
    def __init__(self, timetable, term: Term, name: str, teacher: Teacher, year: int, full_time: bool = True):
        from DeanerySystem.timetable2 import Timetable2
        if not type(timetable) == Timetable2: raise Exception("Timetable must be type of `Timetable2`.")
        self._timetable = timetable
        self._term = term
        self._name = name
        self._year = year
        self._full_time = full_time
        self.__teacher = teacher

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def setTeacher(self, value):
        if type(value) != Teacher:
            raise LessonError("Teacher must be Teacher type.")    
        self.__teacher = value

    @teacher.deleter
    def delTeacher(self):
        self.__teacher = None

    @property
    def timetable(self):
        return self._timetable

    @timetable.setter
    def setTimetable(self, timetable):
        from DeanerySystem.timetable2 import Timetable2
        if type(timetable) != Timetable2:
            raise LessonError("Timetable must be Timetable2 type.")
        self._timetable = timetable

    @property
    def term(self):
        return self._term

    @term.setter
    def setTerm(self, term):
        if type(term) != Term:
            raise LessonError("Term must be Term type.")
        self._term = term

    @property
    def name(self):
        return self._name

    @name.setter
    def setName(self, name):
        if type(name) != str:
            raise LessonError("Name must be a string.")
        self._name = name

    @property
    def teacherName(self):
        return self._teacher_name

    @teacherName.setter
    def setTeacherName(self, name):
        if type(name) != str:
            raise LessonError("Teacher name must be a string.")
        self._teacher_name = name

    @property
    def year(self):
        return self._year

    @year.setter
    def setYear(self, year):
        if type(year) != int:
            raise LessonError("Year mus be an intiger.")
        self._year = year

    @property
    def fullTime(self):
        return self._full_time

    @fullTime.setter
    def setFullTime(self, full_time):
        if type(full_time) != bool:
            raise LessonError("Full_time property must be bool.")
        self._full_time = full_time

    def earlierDay(self):
        new_day = Day(7 if self._term._day.value - 1 == 0 else self._term._day.value - 1)
        new_term = Term(self._term._hour, self._term._minute, self._term._duration, new_day)

        if self._timetable.can_be_transferred_to(new_term, self._full_time):
            self._term._day = new_day
            return True
        else:
            return False

    def laterDay(self):
        new_day = Day(1 if self._term._day.value + 1 == 8 else self._term._day.value + 1)
        new_term = Term(self._term._hour, self._term._minute, self._term._duration, new_day)

        if self._timetable.can_be_transferred_to(new_term, self._full_time):
            self._term._day = new_day
            return True
        else:
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

        isOnBreak = self.timetable.onBreak(new_term)

        if isOnBreak[0]:
            new_min -=  isOnBreak[1]
            if new_min < 0:
                new_hour -= 1
                new_min = 60 + new_min
            new_term = Term(new_hour, new_min, self._term._duration, self._term._day)

        if self._timetable.can_be_transferred_to(new_term, self._full_time):
            self._term._hour = new_hour
            self._term._minute = new_min
            return True
        else:
            return False        

    def laterTime(self):
        hour_d = self._term._duration // 60
        min_d = self._term._duration % 60

        new_hour = self._term._hour + hour_d
        new_min = self._term._minute + min_d
        if new_min >= 60:
            new_hour += 1
            new_min = new_min - 60

        new_term = Term(new_hour, new_min, self._term._duration, self._term._day)

        isOnBreak = self.timetable.onBreak(new_term)

        if isOnBreak[0] and not self.timetable.skipBreaks:
            print("self.skipBreaks is set to False. Can't move lesson")
            return False

        if isOnBreak[0]:
            new_min += isOnBreak[1]
            if new_min >= 60:
                new_hour += 1
                new_min = new_min - 60
            new_term = Term(new_hour, new_min, self._term._duration, self._term._day)

        if self._timetable.can_be_transferred_to(new_term, self._full_time):
            self._term._hour = new_hour
            self._term._minute = new_min
            return True
        else:
            return False

    def __add__(self, teacher):
        if self.teacher == teacher:
            return False
        if type(teacher) == Teacher:
            total_time = self._timetable.getTotalHours(teacher) + (self.term.duration // 45)*45 + (self.term.duration % 45)
            if total_time <= 6*45:
                self.__teacher = teacher
                return True
        return False

    def __sub__(self, teacher):
        if type(teacher) == Teacher and teacher.id == self.teacher.id:
            self.__teacher = Teacher(None, None)
            return True
        return False

    def __str__(self):
        return "{} ({})\n{} rok studiów {}\nProwadzący: {} {}".format(self._name, self._term, self._year, "stacjonarnych" if self._full_time else "niestacjonarnych", self.teacher.imie, self.teacher.nazwisko)