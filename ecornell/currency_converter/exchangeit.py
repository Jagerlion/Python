"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Bryan Ruiz
Date: 12/19/2023
"""

import currency

# get the input values first
src = input('3-letter code for original currency: ')
dst = input('3-letter code for the new currency: ')
amt = float(input('Amount of the original currency: '))


# get the exchange
value = currency.exchange(src, dst, amt)

# return the exchange value with a formatted print statement
print(f'You can exchange {amt} {src} for {value:.3f} {dst}.')
