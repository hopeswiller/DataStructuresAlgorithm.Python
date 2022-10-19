# Keeping the scores of a baseball game. The scores of previous rounds affect the scores of the current rounds.
# Beginnning of the game you start with an empty record. You are given a list of strings ops.
# where ops[i] is the ith operation you must apply to the record. i is given as
# x  - an integer. Record a new score of x
# D  - Record a new score that is double the previous score. Previous score is always guranteed
# +  - Record a new score that is the sum of the previous two scores. Previous two scores are always guranteed
# C  - Ivalidate the previous score and remove from record.Previous score is always guranteed
# Return the sum of the scores in record.


def calcPoints(ops) -> int:
    result = None

    dummies = ["C", "D", "+"]
    record = []
    for i in range(len(ops)):
        if not ops[i] in dummies:
            record.append(int(ops[i]))

        else:
            if ops[i] == "D":
                # double the previous score in record
                tmp = 2 * record[-1]
                record.append(tmp)

            if ops[i] == "C":
                # remove the previous score in record
                record.pop()

            if ops[i] == "+":
                # sum the previous two scores in record
                tmp = record[-1] + record[-2]
                record.append(tmp)

    print(record)
    result = sum(record)
    return result


if __name__ == "__main__":
    line = input("Enter input:")
    ops = line.strip().split()

    print(calcPoints(ops))
