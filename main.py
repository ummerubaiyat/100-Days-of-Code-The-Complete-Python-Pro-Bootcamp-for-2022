#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill= float(input("Whats was the total bill? $"))
tip = int(input("How much tip you would you like to give? 10,12,15?"))
bill_with_tip= bill*(tip/100)+bill
bill_with_tip= (bill_with_tip/5)  
final_bill= round(bill_with_tip,2)
print(f"Each person should pay{final_bill}" )