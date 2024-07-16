# Write a program to print the range of dates from today to the given date.

from datetime import date

# Get today's date
today = date.today()
# print(" \n Today's date : ",today,"\n")

# Get year, month, day from user input
print(f" \n *** Please enter the date in yyyy-mm-dd format. ***  --->  Example : {today} \n ")
year = int(input("Enter the year (4 digits) : "))
month = int(input("Enter the month (01-12) : "))
day = int(input("Enter the day (01-31) : "))

input_date = date(year, month, day)

# Join input date with "-" {02 is format date with two numbers - zero}
given_date = f"{year}-{month:02}-{day:02}" 

print(f'\n Today\'s date : {today} and Given date : {given_date}')

diff = (input_date - today).days

if diff < 0:
    print(f'\n {-diff} days before today.')
elif diff == 0:
    print(f'\n Today {diff} no difference.')
elif diff > 0:
    print(f'\n The date {given_date} is {diff} days after today.')
else:
    print(None)
