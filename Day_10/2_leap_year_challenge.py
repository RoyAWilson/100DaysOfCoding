def is_leap_year(year):
    '''Calculate if a year is a leap year

    '''

    if year % 4 != 0:
        return f'Year {year} is not a leap year'
    elif year % 100 == 0 and year % 400 == 0:
        return f'Year {year} is a leap year'
    elif year % 100 != 0 and year % 4 == 0:
        return f'Year {year} is a leap year'
    else:
        return f'Year {year} is not a leap year'


check = int(input('Which year do you need to check?  > '))
print(is_leap_year(check))

# Works on my machine but not on the portal used in the course.
