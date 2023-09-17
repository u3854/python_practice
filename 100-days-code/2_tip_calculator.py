#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
group_size = int(input("How many people to split the bill? "))

total_bill = (100 + tip) / 100 * bill

print("Each person should pay: ${:.2f}".format(total_bill / group_size))