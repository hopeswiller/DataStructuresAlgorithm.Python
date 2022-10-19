# every element in the list is the number of goals scored by each team
# in a match
# e.g: team B has scored 2 and 3 goals in the first and second match respectively
# Question: Compute the number of matches where team A has scored less or equal goals
# team B has scored in the same match
def counts(teamA, teamB):
    # Write your code here

    res = []
    for b in range(len(teamB)):
        goals, matches = 0, 0
        for a in range(len(teamA)):
            goals += teamA[a]
            matches += 1

            if goals <= teamB[b]:
                continue
            else:
                break

        res.append(matches)

    return res


print(counts([1, 2, 3], [2, 4]))
