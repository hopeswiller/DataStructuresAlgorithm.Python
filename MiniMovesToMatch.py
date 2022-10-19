# minimum moves to match arr1 to arr2; moves maybe decrement or increament
# comparing 1234 to 2345 results in 4 moves
# increment 1 once to get 2 - 1 move
# increment 2 once to get 3 - 1 move
# increment 3 once to get 4 - 1 move
# increment 4 once to get 5 - 1 move
#
# comparing 4231 to 3214 results in 6 moves
# decrement 4 once to get 3 - 1 move
# decrement 3 twice to get 1 - 2 moves
# increment 1 thrice to get 4 - 3 moves

# In total we make 10 moves to match the arrays
# arr1 = [1234,4231]
# arr2 = [2345,3214]


def minimumMoves(arr1, arr2):
    # Write your code here
    moves = 0
    # loop through each array at the same time
    for a, b in zip(arr1, arr2):
        # break each element into list
        a1 = list(map(int, "".join(str(a))))
        b1 = list(map(int, "".join(str(b))))

        print(a1, b1)
        idx = 0

        # compare each digit of an element to perform move
        while idx < len(a1):
            if b1[idx] >= a1[idx]:
                moves += b1[idx] - a1[idx]
            else:
                moves += a1[idx] - b1[idx]
            idx += 1

    return moves


moves = minimumMoves([1234, 4231], [2345, 3214])
print(moves)
