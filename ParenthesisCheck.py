# Using Stacks

open_list = "([{<"
close_list = ")]}>"

map = dict(zip(open_list, close_list))

# Function to check parenthesis
def checkParenthesis(item):
    stack = []
    # take every parenthesis in the string
    for i in item:
        if i in open_list:
            stack.append(i)
        else:
            if len(stack) > 0 and map.get(stack[-1]) == i:
                stack.pop()
            else:
                return "Unbalanced"

    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


arr = ["{[]{()}}<>", "[(<{}{}>)][()]", "((()"]
for i in arr:
    print(i, "-", checkParenthesis(i))
