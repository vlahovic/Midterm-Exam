"""
===================   TASK 1   ====================
* Name: Area Of Circle
*
* Write a function `area_of_circle` that will
* return area enclosed by a circle of radius `r`.
* Consider that only float value for radius will
* be passed. Negative values should be considered
* as typo and function should ignore sign of a
* number.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""
import math

def area_of_circle(r):

    if not isinstance(r, float) and not isinstance(r, int): # unijeti broj mora biti cijeli ili decimalni, pa to ispitujemo,
        return -1                                           # a ako nije vratice -1

    return (abs(r)**2)*math.pi  #f-ja vraca povrsinu kruga datog poluprecnika


def main():

    povrsina = area_of_circle(-2.3)
    print(povrsina)

    pass

main()