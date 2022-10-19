colors = "red2 green5 yellow3 blue1"


def orderColors(colorStr) -> str:
    """Return original colors names"""

    result = ""
    colors = colorStr.split()
    print(f"current order : {colors}")

    # using insertion sort
    for i in range(1, len(colors)):

        key = colors[i]
        marker = i - 1

        while marker >= 0 and key[-1] < colors[marker][-1]:
            # then swap
            colors[marker + 1] = colors[marker]
            marker -= 1
        colors[marker + 1] = key

    for i in colors:
        result += i[:-1] + " "

    return result


print(orderColors(colors))
