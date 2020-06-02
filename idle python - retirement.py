#Create variables
retirement_age = 65

birth_year = int(input("please enter your year of birth"))
current_year = 2020

#Calculate and print the results
age = current_year - birth_year
print("you are {} years old".format(age))

#Add an if statement
if age == retirement_age:
    print("you have reached retirement age")
