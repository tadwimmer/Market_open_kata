class Holiday:

    def __init__(self, rule, day_or_week, month):
        self._rule = rule
        self._day_or_week = day_or_week
        self._month = month

    def __str__(self):
        return 'Holiday: rule ' + self._rule+' occurance '+ str(self._day_or_week)+' month ' +  str(self._month)

    def __eq__(self, other):
        if(isinstance(other, Holiday)):
            return self._rule == other._rule and self._day_or_week == other._day_or_week and self._month == other._month

holidays = [Holiday('Monday', 3, 1), Holiday('Monday', 3, 2)]

MON = 1

JAN = 1
FEB = 2

def is_market_open(date):
    day_of_week = int(date.strftime("%w"))
    month = int(date.strftime('%m'))
    day_of_month = int(date.strftime('%d'))
    week = week_of_occurrance(day_of_month)
    if day_of_week == 0 or day_of_week == 6:
        return False
    elif month == JAN and (day_of_month == 1 or (day_of_week == MON and day_of_month == 2)):
        return False
    elif is_monday_holiday(month, week):
        return False
    return True


def week_of_occurrance(day_of_month):
    return int(day_of_month / 7) if day_of_month %7 == 0  else int(day_of_month / 7) + 1

def is_monday_holiday(month, week):
    # Monday Holidays
    holiday = Holiday('Monday', week, month)
    return True if holiday in holidays else False
