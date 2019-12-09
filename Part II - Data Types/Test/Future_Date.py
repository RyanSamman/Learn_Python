
# Static Dictionary/Lists:
# Converts Alphanumeric days of the week to Numeric
dayBankAN = {"Sunday": 0,
             "Monday": 1,
             "Tuesday": 2,
             "Wednesday": 3,
             "Thursday": 4,
             "Friday": 5,
             "Saturday": 6}
# Numeric to Alphanumeric
dayBankNA = ["Sunday",
             "Monday",
             "Tuesday",
             "Wednesday",
             "Thursday",
             "Friday",
             "Saturday"]

y = "Yes" # if y =/ "Yes" Then it will exit the program

while y == "Yes":
    # inputs
    dayOfWeek = input("Input current day: ") # Worded day of the week (Sunday Monday etc..)
    daysFromNow = int(input("Days from now: ")) # Days from day of the week earlier input

    # Converts the input day of the week to number form
    dayOfWeekNo = dayBankAN[dayOfWeek]

    # Processes day outputting a numeric future day of the week
    futureDateN = (dayOfWeekNo + daysFromNow) % 7

    # print(futureDate) #DEBUGGING

    futureDateA = dayBankNA[futureDateN]
    print(futureDateA)
    y = input("Continue (Yes): ") # If anything other than "Yes", program will terminate


    # ~~~~ Scrap Code ~~~~~~
# if futureDate is not 0:
#    print(dayBankNA[futureDate])
# else:
#    print(dayOfWeek)


