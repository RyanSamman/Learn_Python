# Inbuts
dayToday = eval(input("Enter today's day: "))
daysElapsed = eval(input("Enter the number of days elapsed since today: "))

# Brosessing
dayFuture = (dayToday + daysElapsed)

# Oudbut
if dayFuture == 0:
    print("The future date is Saturday")
elif dayFuture == 1:
    print("The future date is Monday")
elif dayFuture == 2:
    print("The future date is Tuesday")
elif dayFuture == 3:
    print("The future date is Wednesday")
elif dayFuture == 4:
    print("The future date is Thursday")
elif dayFuture == 5:
    print("The future date is Friday")
elif dayFuture == 6:
    print("The future date is Saturday")
