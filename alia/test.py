try:
    user_num = input()
    user_num = int(user_num)
except ValueError:
    print(f"Input Exception: invalid literal for int() with base 10: '{user_num}'")
try:
    div_num = input()
    div_num = int(div_num)
except ValueError:
    print(f"Input Exception: invalid literal for int() with base 10: '{div_num}'")
try:

except ZeroDivisionError:
    print('Zero Division Exception: integer division or modulo by zero')
else:
    print(quotient)