# This program will prompt the user to enter a month number, then it will read month sales
# file and tell the user the sales total for that month as well as the total sales for the
# year.
# Chris Blaylock
# 11/19/2019


# Var for the total, and for the data file list. 
total = 0
#monthlySalesNumbers = []

# Creates a list that contains the 12 names of the months.
month_list = ['January', 'February', 'March', 'April', 'May', 'June',
             'July', 'August', 'September', 'October', 'November', 'December']



# Read data from file
infile = open("monthlySales.txt",'r')

# Use split lines to seperate the data.
monthlySalesNumbers = infile.read().splitlines()

# Use a for loop to convert the str data into float data, while also figuring out
# the total annual sales.
index = 0
while index < len(monthlySalesNumbers):
    monthlySalesNumbers[index] = float(monthlySalesNumbers[index])
    index += 1

for num in monthlySalesNumbers:
    number = float(num)
    total = total + number

# Close the file.
infile.close()

# Input: Prompt the user to enter a month number. 
enteredMonth = int(input("Enter a month number (1-12): "))

# Use a while loop to make sure the user is inputing a correct number. 
while (enteredMonth > 12 or enteredMonth < 1 ):
        print ("Invalid entry.", end =" ")
        enteredMonth = int(input("Enter a month number (1-12): "))
        
# Output: print the month name by subtracting 1 because of the index starting from 0.
print ("The",month_list[enteredMonth - 1], "sales total is: ", format(monthlySalesNumbers[enteredMonth - 1],",.2f"))
print ("The annual sales total is: ", (format(total, ",.2f")))

