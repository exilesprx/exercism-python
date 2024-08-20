def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps = 0
    while True:
        if number == 1:
            return steps

        elif number % 2 == 0:
            number //= 2

        else:
            number = 3 * number + 1

        steps += 1
