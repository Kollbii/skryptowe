from DeanerySystem.base_term import BaseTerm


class Break(BaseTerm):
    '''Przerwy w tym samym czasie przez wszystkie dni tygodnia'''
    def __init__(self, term: BaseTerm):
        super().__init__(hour=term.hour, minute=term.minute, duration=term.duration)

    def __str__(self):
        return "Przerwa"

    def getTerm(self):
        return [(self.hour, self.minute), self.duration]