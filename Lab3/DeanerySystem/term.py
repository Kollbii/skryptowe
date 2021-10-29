from DeanerySystem.day import Day

class Term(object):

    def __init__(self, day, hour, minute):
        self.hour = hour
        self.minute = minute 
        self.duration = 90
        self._day = day

    def __str__(self):
        rep_day = { 1: "Poniedziałek",
                    2: "Wtorek",
                    3: "Środa",
                    4: "Czwartek",
                    5: "Piątek",
                    6: "Sobota",
                    7: "Niedziela",
        }[self._day.value]
        return "{} {}:{} [{}]".format(rep_day, self.hour, self.minute, self.duration)

    def earlierThan(self, termin):
        day_diff = self._day.difference(termin._day)
        if day_diff > 0:
            return True
        elif day_diff == 0:
            return False if termin.hour < self.hour else (False if termin.hour == self.hour and termin.minute < self.minute else True) 
        return False

    # Way easier to just negate this ^ func
    def laterThan(self, termin):
        return not self.earlierThan(termin)

    def equals(self, termin):
        return True if self._day.difference(termin._day) == 0 and self.hour == termin.hour and self.minute == termin.minute else False

    
    def getDay(self, day, month, year):
        offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        week   = ['Sunday', 
                'Monday', 
                'Tuesday', 
                'Wednesday', 
                'Thursday',  
                'Friday', 
                'Saturday']
        afterFeb = 1
        if month > 2: afterFeb = 0
        aux = year - 1700 - afterFeb
        dayOfWeek = 5
        dayOfWeek += (aux + afterFeb) * 365                  
        dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400     
        dayOfWeek += offset[month - 1] + (day - 1)               
        dayOfWeek %= 7
        return int(dayOfWeek)

    def unpackDate(self, napis):
        data = napis.split(" ")
        day_diff = int(data[5]) - int(data[0])
        months = {'I':1, "II":2, "III":3,"IV":4,"V":5, "VI":6, "VII":7, "VIII":8, "IX":9, "X":10, "XI":11,"XII":12}
        month_dif = months[data[6]] - months[data[1]]
        hour2 = data[8].split(":")
        hour1 = data[3].split(":")
        hour_diff = int(hour2[0]) - int(hour1[0])
        min_diff = int(hour2[1]) - int(hour1[1]) 

        raise NotImplementedError

    def setTerm(self, napis):
        data = napis.split(" ")
        day_diff = int(data[5]) - int(data[0])
        months = {'I':1, "II":2, "III":3,"IV":4,"V":5, "VI":6, "VII":7, "VIII":8, "IX":9, "X":10, "XI":11,"XII":12}
        month_dif = months[data[6]] - months[data[1]]
        hour2 = data[8].split(":")
        hour1 = data[3].split(":")
        hour_diff = int(hour2[0]) - int(hour1[0])
        min_diff = int(hour2[1]) - int(hour1[1]) 

        time_in_minutes = month_dif*30*24*60 + day_diff*24*60 + hour_diff*60 + min_diff 

        new_day = self.getDay(int(data[0]), months[data[1]], int(data[2]))
        rep_day = { 1: Day.MON,
                    2: Day.TUE,
                    3: Day.WED,
                    4: Day.THU,
                    5: Day.FRI,
                    6: Day.SAT,
                    7: Day.SUN,
        }[new_day]

        try:
            self.hour = int(hour1[0])
            self.minute = int(hour1[1])
            self.duration = time_in_minutes
            self._day = rep_day
        except Exception:
            return False
        else:
            return True