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

class FixedHoliday(Holiday):

    def __init__(self, day, month, shift=''):
        self._rule = 'Fixed'
        self._day_or_week = day
        self._month = month
        self._shift = shift

holidays = [Holiday('Monday', 3, 1), Holiday('Monday', 3, 2),
            Holiday('Monday', 1, 9), FixedHoliday(1, 1, 'fwd'),
            FixedHoliday(19, 6, 'both'), FixedHoliday(4, 7, 'both'),
            FixedHoliday(25, 12, 'both')]

SUN = 0
MON = 1
THURS = 4
FRI = 5
SAT = 6

MAY = 5
NOV = 11

def is_market_open(date):
    '''
    Determines if the NYSE is open on the given date
    :param date: The date to check
    :return: True if the NYSE is open, False if the date is a
    weekend or a markey holiday.
    '''
    day_of_week = int(date.strftime("%w"))
    month = int(date.strftime('%m'))
    day_of_month = int(date.strftime('%d'))
    occurrrance = day_occurrance(day_of_month)
    if day_of_week == SUN or day_of_week == SAT:
        #Saturday or Sonday
        return False
    elif is_fixed_holiday(month, day_of_month):
        return False
    elif day_of_week == MON:
        if month == MAY and day_of_month > 24 or \
                is_monday_observance(month, day_of_month) or \
                is_monday_holiday(month, occurrrance):
            return False
    elif day_of_week == THURS and month == NOV and occurrrance == 4:
        #Thanksgivomg
        return False
    elif day_of_week == FRI and is_friday_observance(month, day_of_month):
        return False
    return True

def is_fixed_holiday(month, day):
    candidate = FixedHoliday(day, month)
    return True if candidate in holidays else False

def is_friday_observance(month, day):
    # Fixed holiday falls on Saturday, observed on Friday
    return is_fixed_holiday(month, day + 1)

def is_monday_observance(month, day):
    #Fixed holiday falls on Sunday, observed on Monday
    return is_fixed_holiday(month, day - 1)

def is_monday_holiday(month, week):
    # Monday Holidays
    holiday = Holiday('Monday', week, month)
    return True if holiday in holidays else False

def day_occurrance(day_of_month):
    '''
    Determines which occurrance of the weekday within the month
    the given day of the month falls on
    :param day_of_month (int): The day of the month
    :return: Which occurrance of the weekday the day fallso on, e.g
    third Monday, etc.
    '''
    return int(day_of_month / 7) if day_of_month %7 == 0  else int(day_of_month / 7) + 1


