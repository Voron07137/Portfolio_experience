def is_year_lip(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(True)
    else:
        print(False)


god = 2004
is_year_lip(god)  # True
god = 2100
is_year_lip(god)  # False
god = 2005
is_year_lip(god)  # False
god = 2000
is_year_lip(god)  # True
