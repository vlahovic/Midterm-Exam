"""
===================   TASK 4   ====================
* Name: Convert To Upper
*
* Write a function `convert_2_upper` that will take
* a string as an argument. The function should
* convert all lowercase letter to uppercase without
* usage of built-in function `upper()`.

* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""
def convert_2_upper(recenica):
    g = ""
    for ch in recenica:
        if ord(ch) >= 97 and ord(ch) <= 122:
            x = ord(ch) - 32
            y = chr(x)
            g = g + y
    return g
def main():
    recenica = input('Enter here: ')
    print(convert_2_upper(recenica))


main()