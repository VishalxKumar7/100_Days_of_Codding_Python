print("Welcome to the tiip calculator!")
bill = float(input("What is the total bill $: "))
tip_per = int(input("What percentage tip would you like to give:"))
people = int(input("How many people to split the bill? :"))

tip = round((bill / 100 * tip_per),2)
total_bill = round((bill + tip),2)
per_person_bill = round((total_bill / people),2)

print(f"Tip: {tip}")
print(f"Total Bill {total_bill}")
print(f"Bill Per Person {per_person_bill}")