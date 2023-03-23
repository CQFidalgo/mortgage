# Python script that computes the amortization table of a mortgage based in the Sergi Almacellas Challenge:
# https://gitlab.com/-/snippets/2515187
# Author CQFidalgo.

# Import statements
import csv

# Declare and initialize variables
month = 1          # initial month
total_mortgage = actual_mortgage = 10000
monthly = 375
yearly = 500
interest = 0.005

# Create the CSV file and write the header row
with open('mortgage.csv',mode='w',newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Month','Interest','Due','Due + Interest','To Pay']) #Header

# Calculate mortgage, print the results, and write them to the file
with open('mortgage.csv',mode='a',newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Loop until the mortgage is fully paid
    while actual_mortgage > 0:
        # Calculate the interest amount for the current month
        interest_amount = actual_mortgage * interest

        # Calculate the total amount due for the current month
        due_plus_interest = actual_mortgage + interest_amount

        # Determine the amount to pay for the current month, considering whether it's an annual payment
        if (month % 12 != 0):                        #When the result is 0, the annual fee must be paid
            to_pay = monthly
        else:
            to_pay = monthly + yearly

        # Write the current month's data to the CSV file
        writer.writerow([month, f"{interest_amount:.2f}", f"{actual_mortgage:.2f}", f"{due_plus_interest:.2f}", f"{to_pay:.2f}"])
        # Print the current month's data to the console
        print(f"Month {month}, Interest {interest_amount:.2f}, due: {actual_mortgage:.2f}, due + interest {due_plus_interest:.2f}, to pay {to_pay:.2f}")
        # Update the mortgage amount for the next month
        actual_mortgage = due_plus_interest - to_pay
        # Increment the month counter
        month += 1