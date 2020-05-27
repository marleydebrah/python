#Create variable
hours_spent = int(input("How many hours do you spend on the internet"))

#Print the result
print("you spend {} hours on the internet." .format(hours_spent))

#Add if/else statements based around results
if hours_spent <3:
    print("That's a healthy amount of time.")

elif hours_spent >=3 and hours_spent <=5:
    print("Make sure you have some exercise as well!")

elif hours_spent >5 and hours_spent <=24:
    print("Yikes, there are only 24 hours in a day!")
