print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))/100
people = int(input("How many people to split the bill? "))

tipresult = round((total/people) + (total*tip)/people,2)

print("Each person should pay: $" + str(tipresult))