"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime
todays_date = datetime.date.today()

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    first_day_of_birth_month = datetime.date(year, month, 1)
    current = month % 12
    if current == 0:
        year = year + 1
    one_month_after_birth = datetime.date(year, current + 1, 1)
    difference = one_month_after_birth - first_day_of_birth_month
    return difference.days



print(days_in_month(2017,2))



def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    
    if datetime.MINYEAR <= year < datetime.MAXYEAR and 0 < month < 13:
        days = (days_in_month(year, month))
    else:
        return False
    if 0 < day <= days:
        return True
    else:
        return False

print(is_valid_date(2017, 1, 1))




def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if is_valid_date(year1, month1,  day1) == False:
        return 0
    elif is_valid_date(year2, month2,  day2) == False:
        return 0
    else:
        oldest_date = datetime.date(year1, month1, day1)
        newest_date = datetime.date(year2, month2, day2)
        difference_between_em = newest_date - oldest_date
        if difference_between_em.days < 0:
            return 0
        else:
            return difference_between_em.days
        
        
        
        
print(days_between(2005,2,23,2007,9,22))







def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if is_valid_date(year, month, day) == False:
        return 0
    else:
        your_birthday = datetime.date(year, month, day)
        if your_birthday > todays_date:
            return 0  
        else:
            your_age = todays_date - your_birthday
            return your_age.days

print(age_in_days(2017, 1, 1))