#  find most common digit in a list
# Divide each number by 10
# store right side of the decimal and proceed with step 1 & 2 until its zero

from collections import Counter

nums = [232, 67, 54, 26, 92, 61, 55, 42, 95, 100]


def findme(nums=nums):
    b = []
    for num in nums:
        while num > 0:
            # get last digit of the number
            b.append(int(num % 10))
            # remove the last digit from the number
            num = int(num / 10)

    print(b)
    freq = Counter(b)
    print(freq)
    print(freq.most_common(1))


findme()
