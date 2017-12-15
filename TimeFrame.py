from datetime import *; from dateutil.relativedelta import *
import calendar


date_of_month = 25

class TimeFrame():

    def __init__(self):
        self.periods= []

    def calculate_dates(self, no_of_periods, period ='month'):

        today = date.today()

        day_of_month = date(day=date_of_month, month=today.month, year=today.year)
        if day_of_month >= today:
            day_of_month = day_of_month + relativedelta(months=-1)

        if period == 'months':
            for i in range(0, no_of_periods):
                if day_of_month.weekday() > 4:
                    tempday = day_of_month + relativedelta(weekday=FR(-1))
                    self.periods.append(tempday)
                else:
                    self.periods.append(day_of_month)
                day_of_month = day_of_month + relativedelta(months=-1)




#
# t = TimeFrame()
# t.calculate_dates(12)
# for i in t.periods:
#     print (i)