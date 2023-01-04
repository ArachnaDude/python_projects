def is_year_leap(year):
  if year < 1582: 
    print("Not within the Gregorian calendar period")
    return None
  elif year % 4 != 0: return False
  elif year % 100 != 0: return True
  elif year % 400 != 0: return False
  else: return True 

def days_in_month(year, month):
  month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  leap_year_bool = is_year_leap(year)
  if month <=0 or month > 12: return None

  if leap_year_bool:
    month_lengths[1] = 29

  return month_lengths[month - 1]


def day_of_year(year, month, day):

  number_of_days = 0
  month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  leap_year_bool = is_year_leap(year)
  if leap_year_bool:
    month_lengths[1] = 29

  month_length = days_in_month(year, month)

  if month_length == None: 
    print("That's not a month")
    return None
  if day <= 0 or day > month_length: 
    print("That month doesn't have that many days")
    return None

  for i in range(month - 1):
    number_of_days += month_lengths[i]
  number_of_days += day
  return number_of_days

  

print(day_of_year(2000, 1, 11))