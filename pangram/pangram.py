def is_pangram(sentence):
    letters = [0 for _ in range(26)]

    for letter in sentence:
        if not letter.isalpha():
            continue

        letters[ord(letter.lower()) - 97] = 1

    return sum(letters) == 26
