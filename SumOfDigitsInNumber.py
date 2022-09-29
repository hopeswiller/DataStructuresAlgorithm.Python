# Declare a variable to store the sum and set it to 0
# Get the rightmost digit of the number with help of the remainder ‘%’ operator by dividing it by 10 and add it to sum.
# Divide the number by 10 with help of ‘/’ operator to remove the rightmost digit.

num = 1980


def sumOfDigits(n):
    sum = 0
    while n != 0:
        # print(int(n % 10), " -", n % 10)
        sum += int(n % 10)
        n = int(n / 10)
    return sum


print(sumOfDigits(num))


# using Recursion
def sumOfDigitsRecursion(n):
    if n == 0:
        return 0
    else:
        n = int(n / 10)
        return int(n % 10) + sumOfDigitsRecursion(n)


print(sumOfDigitsRecursion(num))
