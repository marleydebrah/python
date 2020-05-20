#Create variables
hourly_rate = float(input("how much do you earn per hour?"))
hours_worked = int(input("please enter number of hours you have worked this week?"))

#Calculate wages based on hourly_rate and hours_worked
weekly_pay = hourly_rate * hours_worked
weekly_pay *= 0.8
annual_pay = weekly_pay * 52

#Print the result
print("your weekly income is {}" .format(weekly_pay))
print("your annual income is {}" .format(annual_pay))

#Add if/else statements based around results
if annual_pay <=34000:
    print("you have a low income")
elif annual_pay <=50000:
    print("you have a medium income")
