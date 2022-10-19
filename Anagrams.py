# Given an array of strings,
# return all groups of strings that are anagrams.

# The groups must be created in order of their appearance in the original array. Look at the sample case for clarification.
# {act,god,cat,dog,tac}
# Note: The final output will be in lexicographic order.


words = ["act", "god", "cat", "dog", "tac"]


def anagrams(words):
    dict = {}
    for word in words:

        # take each word in the list and sort its letters
        sorted_word = "".join(sorted(word))
        print(sorted_word)

        # group words of the same sort/letters in a dict
        if sorted_word in dict.keys():
            dict[sorted_word].append(word)
        else:
            dict[sorted_word] = []
            dict[sorted_word].append(word)

    print(dict)


anagrams(words)
