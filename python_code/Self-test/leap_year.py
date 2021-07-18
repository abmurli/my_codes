def is_leap(year):
    leap = False
    print(year%400)
    if year % 4 == 0 or year % 400 == 0:
        leap = True
    if year % 100 and year % 400 != 0:
        leap = False

    return leap


year = int(input())

leap_year = is_leap(year)
print(leap_year)