from day import Day

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
        return "{} {}:{} [{}]".format(rep_day, self.hour, "00" if self.minute == 0 else self.minute, self.duration)

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


    # "27 X 2021 8:10 - 27 X 2021 8:30"
    def unpackDate(self, napis):
        data = [napis.strip() for napis in napis.split(" ")]
        months = {'I':1, "II":2, "III":3, "IV":4, "V":5, "VI":6, "VII":7, "VIII":8, "IX":9, "X":10, "XI":11, "XII":12}
        
        year1 = int(data[2])
        year2 = int(data[7])

        day1 = int(data[0])
        day2 = int(data[5])
        
        month1 = months[data[1]]
        month2 = months[data[6]]
        
        hour1 = int(data[3].split(":")[0])
        min1 = int(data[3].split(":")[1])
        
        hour2 = int(data[8].split(":")[0])
        min2 = int(data[8].split(":")[1])
        
        #TODO Check if valid date
        return [[day1, month1, year1, hour1, min1], [day2, month2, year2, hour2, min2]]

    def setTerm(self, napis):
        data = self.unpackDate(napis)

        year_d  = data[1][2] - data[0][2]
        month_d = data[1][1] - data[0][1]
        day_d   = data[1][0] - data[0][0]
        hour_d  = data[1][3] - data[0][3]
        min_d   = data[1][4] - data[0][4]
        
        time_in_minutes = year_d*365*24*60 + month_d*30*24*60 + day_d*24*60 + hour_d*60 + min_d 
        
        new_day = { 1: Day.MON,
                    2: Day.TUE,
                    3: Day.WED,
                    4: Day.THU,
                    5: Day.FRI,
                    6: Day.SAT,
                    7: Day.SUN,
        }[self.getDay(data[0][0], data[0][1], data[0][2])]

        try:
            self.hour = data[0][3]
            self.minute = data[0][4]
            self.duration = time_in_minutes
            self._day = new_day
        except Exception:
            return False
        else:
            return True