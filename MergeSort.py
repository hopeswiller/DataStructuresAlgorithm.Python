# •    Declare left variable to 0 and right variable to n-1
# •    Find mid by medium formula. mid = (left+right)/2
# •    Call merge sort on (left,mid)
# •    Call merge sort on (mid+1,rear)
# •    Continue till left is less than right
# •    Then call merge function to perform merge sort.

arr = [500, 244, 311, 478, 324, 415, 499, 192, 111, 130, 50, 60, 79]


class MergeSort:
    def __init__(self, arr):
        self.arr = arr
        self.sort(arr)

    def merge(self, arr: list, a: list, b: list):

        i, j, k = 0, 0, 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
            k += 1

        while i < len(a):
            arr[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            arr[k] = b[j]
            j += 1
            k += 1

    def sort(self, arr: list):
        if len(arr) > 1:
            l = 0
            r = len(arr) - 1
            mid = int((l + r) / 2)

            if l <= r:
                #  divide arr with mid and merge sort each half
                # left side
                leftSide = arr[: mid + 1]
                rightSide = arr[mid + 1 :]
                self.sort(leftSide)
                # right side
                self.sort(rightSide)

                self.merge(arr, leftSide, rightSide)
                self.arr = arr

    @staticmethod
    def showSorted():
        print(arr)


MergeSort(arr)
print(MergeSort.showSorted())
