# Declare a variable to store the rev and set it to 0
# Get the rightmost digit of the number with help of the remainder ‘%’ operator by dividing it by 10
# and add it to rev * 10.
# Divide the number by 10 with help of ‘/’ operator to remove the rightmost digit.

num = 123456


def reverse(num: int) -> int:
    rev = 0
    while num != 0:
        rev = (rev * 10) + int(num % 10)
        num = int(num / 10)
    return rev


print(reverse(num))
