arr = [64, 34, 25, 12, 22, 11, 90, 55, 11, 13, 5, 6]
# insertion sort


def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]
        marker = i - 1

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        # of their current position and decrement marker

        while marker >= 0 and key < arr[marker]:
            # then swap
            arr[marker + 1] = arr[marker]
            marker -= 1
        arr[marker + 1] = key

    return arr


res = insertionSort(arr)
print(f"insertionSort : {res}")
