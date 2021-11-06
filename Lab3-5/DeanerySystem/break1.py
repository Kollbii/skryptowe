from DeanerySystem.term import Term


class Break(object):
    '''Przerwy w tym samym czasie przez wszystkie dni tygodnia'''
    def __init__(self, term: Term):
        self.term = term

    def __str__(self):
        return "Przerwa"

    def getTerm(self):
        return [(self.term.hour, self.term.minute), self.term.duration]