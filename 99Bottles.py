# 99 bottles of beer on the wall, 99 bottles of beer
#  Take one down and pass it around, 98 bottles of beer on the wall

# No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, 99 bottles of beer on the wall.


def lyrics(numOfBottles):
    # l = [x for x in range(100)]
    # l.reverse()

    res = ""
    for i in range(numOfBottles, -1, -1):
        if i == 0:
            res += f"\n\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, {numOfBottles} bottles of beer on the wall."
        else:
            res += f"{i} bottles of beer on the wall, {i} bottles of beer"
            res += f"\t\nTake one down and pass it around, {i-1} bottles of beer on the wall\n"

    print(res)


numOfBottles = 99
lyrics(numOfBottles)
