print("Welcome to the tip calculator :")
bill = float(input("What is the total amount of bill ? "))
tip = int(input("What is the tip you would like to give ? "))
people = int(input("Among how many poeple you want to split the bill? "))

new_bill = bill + bill * (tip/100)
bill_per_person = round(new_bill/ people, 2) 
print(f"Your per person bill is {bill_per_person}")