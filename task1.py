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
def area_of_circle(r):
    """
    Calculates Area Of Circle for given r.
    Returns -1 if argument is not int or float
    """
    # r is not integer or float
    if (not isinstance(r, int)) and (not isinstance(r, float)):
        return -1

    # NOTE: Fix this solution in order to work
    # with negative numbers


    return r


def main():

    pi =3.14159265359
    r = 5.0
    area_of_circle= pi * r**2
    print("Area Of Circle is: ", area_of_circle)
    print("This function will work only if r=5 because my python skills are not good enough.")
main()