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
            return False if termin.hour < self.hour else (False if termin.hour == self.hour and termin.minute <= self.minute else True) 
        return False

    # Way easier to just negate this ^ func
    def laterThan(self, termin):
        return not self.earlierThan(termin)

    def equals(self, termin):
        return True if self._day.difference(termin._day) == 0 and self.hour == termin.hour and self.minute == termin.minute else False