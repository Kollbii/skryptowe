from term import Term
from day import Day


term1 = Term(Day.WED, 10, 15)
term2 = Term(Day.TUE, 11, 15)

date1 = "27 X 2021 8:00 - 27 X 2021 8:30"
date2 = "28 X 2021 8:30 - 29 X 2021 8:00"

term1.setTerm(date1)
print(term1)
term2.setTerm(date2)
print(term2)
