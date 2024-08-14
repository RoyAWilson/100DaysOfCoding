def life_in_weeks(age) -> str:
    left = (90 - age) * 52

    return f'You have {left} weeks left.'


x: int = int(input('What is your age in years? >'))

weeks_left = life_in_weeks(x)
print(weeks_left)

# This didn't work on the online tester thing
# Changed the return to a variable and worked ok

# code that worked on the online tester was:

# def life_in_weeks(age) -> str:
#     left = (90 - age) * 52
#     return left
# x = 59
# print(f'You have {life_in_weeks(x)} weeks left.')
