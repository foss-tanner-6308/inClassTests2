def func(year):

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(year, "is a leap year")
                return 1
            else:
                print(year, "is not a leap year")
        else:
            print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
        return 2
