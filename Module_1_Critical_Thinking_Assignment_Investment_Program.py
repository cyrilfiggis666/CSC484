"""
Pseudocode

START

Set principal to 1000
Set rate to 0.07
Set total years to 30

FOR each year from 1 to 30
    Calculate amount using formula:
        amount = principal * (1 + rate)^year
    Display year number and amount
END FOR

END
"""


"""
Investment Growth Calculator

This program calculates the growth of a $1000 investment
earning a 7% annual return over 30 years.
It displays the value of the investment at the end of each year.
"""

# Original amount invested (principal)
principal = 1000

# Annual rate of return (7% expressed as a decimal)
rate = 0.07

total_years = 30

# Loop through years 1 to 30
for year in range(1, total_years + 1):

    # Calculate the investment value using compound interest formula
    amount = principal * (1 + rate) ** year

    print(f"Year {year:2}: ${amount:,.2f}")

