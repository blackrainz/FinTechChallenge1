# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
# YOUR CODE HERE!

# Using len() function to calculate number of loans and save variable number_of_loans
number_of_loans=len(loan_costs)
# Printing the number of loans
print(f"The number of loans is:", + number_of_loans, "loans")

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
# YOUR CODE HERE!

# Using sum() function to calculate sum of all loans and save variable loan_sum
loan_sum=sum(loan_costs)
# Printing sum of loans
print("The sum of all the loans is:", + loan_sum, "$")

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
# YOUR CODE HERE!

# Calculating loan average and saving it as variable loan_average
loan_average=loan_sum / number_of_loans
# Printing average of all loans
print("The average of all the loans is:", + loan_average, "$")

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!

# Using get() to retrieve future_value details from dictionary and store as variable
future_value = loan.get("future_value")
# Printing future value of loan
print("The future value of the loan is:", + future_value, "$")
# Using get() to retrieve remaining_months details from dictionary and store as variable
remaining_months = loan.get("remaining_months")
# Printing remaining months of loan
print("The remaining months on the loan is:", + remaining_months, "months")

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

# YOUR CODE HERE!

# Discount rate
discount_rate = .2
# Calculating present value of loan with present value formula and storing as variable
present_value = future_value / (1 + discount_rate/12) ** remaining_months
# Printing present value of loan
print("The present value of the loan is:", + present_value)

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!

# Using get() to retrieve loan price details from dictionary and store as variable
loan_price = loan.get("loan_price")
# If statement judging if present value is greater or equal to loan price
if(present_value >= loan_price):
    # Printing that the loan is worth it if the present value is greater than or equal to the loan price
    print("The loan is worth the cost to buy it!")
else:
    # Printing that the loan is not worth it if the present value isnt greater than or equal to the loan price
    print("The loan is too expensive and not worth the price.")


"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!

# Defining the calculate_present_value function, with paremeters future_value, remaining_months and annual_discount_rate
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    # Storing annual_discount_rate parameter as a variable
    annual_discount_rate = (annual_discount_rate)
    # Storing future_value parameter as a variable 
    future_value = (future_value)
    # Printing future value
    print("The future value of the loan is:", + future_value, "$")
    # Storing remaining months parameter as a variable
    remaining_months = (remaining_months)
    # Printing remaining months
    print("The remaining months on the loan is:", + remaining_months, "months")
    # Formula for present value
    present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months
    # Returns present_value
    return present_value

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!
# Running calculate_present_value function and storing it as present_value
present_value = calculate_present_value(
    # Parameter for future value below
    new_loan["future_value"],       
    # Parameter for remaining months below
    new_loan["remaining_months"],   
    # Annual discount rate below
    annual_discount_rate = 0.2      
)
print(f"The present value of the loan is: {present_value}")

"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!

# Creating empty list
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!

# for loop to cycle through loans list until end of list
for loan_price in loans:
    # if statement looking for loan price that is less than $500
    if loan_price["loan_price"] <= 500:
        # appending loans less than $500 to the inexpensive_loans list
        inexpensive_loans.append(loan_price)

# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!

# Printing the inexpensive loans list.
print("List of inexpensive loans:", inexpensive_loans)

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!

# Opening the output CSV file using "with open"
with open(output_path, "w", newline='') as csvfile:
    # Create csvwriter
    csvwriter = csv.writer(csvfile, delimiter=",")
    # Write header to file
    csvwriter.writerow(header)
    # for loop to cycle through inexpensive_loans list until end of list
    for loan in inexpensive_loans:
        # Write the values of the inexpensive loans to inexpensive_loans.csv
        csvwriter.writerow(loan.values())