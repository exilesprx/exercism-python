letter_values = {
    **dict.fromkeys("aeioulnrst", 1),
    **dict.fromkeys("dg", 2),
    **dict.fromkeys("bcmp", 3),
    **dict.fromkeys("fhvwy", 4),
    **dict.fromkeys("k", 5),
    **dict.fromkeys("jx", 8),
    **dict.fromkeys("qz", 10),
}


def score(word):
    return sum(map(lambda x: letter_values.get(x.lower(), 0), word))
