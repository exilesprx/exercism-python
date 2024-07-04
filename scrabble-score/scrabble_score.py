def score(word):
    return sum(map(lambda x: letter_value(x.lower()), word))


def letter_value(letter):
    if letter in "aeioulnrst":
        return 1
    if letter in "dg":
        return 2
    if letter in "bcmp":
        return 3
    if letter in "fhvwy":
        return 4
    if letter in "k":
        return 5
    if letter in "jx":
        return 8
    if letter in "qz":
        return 10
    return 0
