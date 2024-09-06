def is_valid(isbn):
    sum = 0
    isbn = isbn.replace('-', '')

    if len(isbn) != 10:
        return False

    for i, c in enumerate(isbn):
        if not c.isdigit():
            if c != 'X' or (c == 'X' and i != 9):
                return False
            else:
                c = 10

        sum += int(c) * (10 - i)

    return sum % 11 == 0

