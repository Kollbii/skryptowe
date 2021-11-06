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
        self._hour = hour

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def setMinute(self, minute):
        self._minute = minute

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def setDuration(self, duration):
        self._duration = duration

    def getEndTime(self):
        hour_d = self._duration // 60
        min_d = self._duration % 60

        new_h = self._hour + hour_d
        new_m = self._minute + min_d

        if new_m > 60:
            new_h += 1
            new_m -= 60
        
        return str(new_h), "0"+str(new_m) if new_m < 10 else str(new_m)

    def getStartTime(self):
        return str(self._hour), "0"+str(self._minute) if self._minute < 10 else str(self._minute)

    def getUniqueStartingHours(self):
        return (self._hour, self._minute)