from DeanerySystem.term_exception import TermError


class BaseTerm(object):
    def __init__(self, hour: int, minute: int, duration: int = 90):
        self._hour = hour
        self._minute = minute 
        self._duration = duration

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def setHour(self, hour):
        if type(hour) is int and hour >= 0 and hour <= 23:
            self._hour = hour
        else:
            raise TermError("Hour must be INT and in between <0; 23>")
        
    @property
    def minute(self):
        return self._minute

    @minute.setter
    def setMinute(self, minute):
        if type(minute) is int and minute >= 0 and minute <= 59:
            self._hour = minute
        else:
            raise TermError("Minute must be INT and in between <0; 59>")

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def setDuration(self, duration):
        if type(duration) is int and duration >= 0:
            self._duration = duration
        else:
            raise TermError("Duration must be positive integer.")

    def earlierThan(self, termin):
        return False if termin._hour < self._hour else (False if termin._hour == self._hour and termin._minute < self._minute else True) 

    def equals(self, termin):
        return True if self._day == termin._day and self._hour == termin._hour and self._minute == termin._minute and self._duration == termin._duration else False
    
    def __lt__(self, termin):
        return self.earlierThan(termin)

    def __le__(self, termin):
        return self.earlierThan(termin) or self.equals(termin)

    def __gt__(self, termin):
        return not self.earlierThan(termin)

    def __ge__(self, termin):
        return not self.earlierThan(termin) or self.equals(termin)

    def __eq__(self, termin):
        return self.equals(termin)

    def __str__(self):
        return "{}:{} [{}]".format(self._hour, self._minute, self._duration)

    def getEndTime(self):
        hour_d = self._duration // 60
        min_d = self._duration % 60

        new_h = self._hour + hour_d
        new_m = self._minute + min_d

        if new_m >= 60:
            new_h += 1
            new_m -= 60
        
        return str(new_h), "0"+str(new_m) if new_m < 10 else str(new_m)

    def getStartTime(self):
        return str(self._hour), "0"+str(self._minute) if self._minute < 10 else str(self._minute)

    def getUniqueStartingHours(self):
        return (self._hour, self._minute)