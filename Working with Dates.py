"""
Welcome
"""
import datetime

def days_in_month(year, month):
    """
    days_in_month
    """
    if month != 12:
        days1 = datetime.date(year, month, 1)
        days2 = datetime.date(year, month+1, 1)
        ans = (days2 - days1).days
    
    else:
        days1 = datetime.date(year, 12, 1)
        days2 = datetime.date(year+1, 1, 1)
        ans = (days2 - days1).days
    return ans
    
def is_valid_date(year, month, day):
    """
    is_valid_date
    """  
    if year > datetime.MAXYEAR or year < datetime.MINYEAR:
        return False

    
    if month > 12 or month < 1:
        return False
  
    if day < 1 or day > days_in_month(year, month):
        return False


    return True

def days_between(year1, month1, day1, year2, month2, day2):
    """
    days_between
    """  
    if not(is_valid_date(year1, month1, day1)) or not(is_valid_date(year2, month2, day2)):
        return 0
    
    if (datetime.date(year2, month2, day2) - datetime.date(year1, month1, day1)).days < 0:
        return 0
    
    days1 = datetime.date(year1, month1, day1)
    days2 = datetime.date(year2, month2, day2)
    
    return (days2-days1).days
    
def age_in_days(year, month, day):
    """
    age_in_days
    """  
    if year == 0:
        return 0
    if not(is_valid_date(year, month, day)):
        return 0
    if  datetime.date(year, month, day) > datetime.date.today():
        return 0
    
    today = datetime.date.today()
    birth = datetime.date(year, month, day)
    age = days_between(birth.year, birth.month, birth.day, today.year, today.month, today.day)
    
    return age
