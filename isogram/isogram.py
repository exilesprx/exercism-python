def is_isogram(string):
    string = ''.join([char for char in string if char.isalpha()])

    return len(string) == len(set(string.lower()))
