def season(mon):
    if mon == 1 or mon == 2 or mon == 12:
        print('Winter')
    if mon == 3 or mon == 4 or mon == 5:
        print('Spring')
    if mon == 6 or mon == 7 or mon == 8:
        print('Summer')
    if mon == 9 or mon == 10 or mon == 11:
        print('Autumn')


month = 2
season(month)
month = 4
season(month)
month = 7
season(month)
month = 11
season(month)
