def response(hey_bob):
    hey_bob = str(hey_bob).strip()
    if len(hey_bob) == 0:
        return "Fine. Be that way!"

    is_question = hey_bob.endswith("?")
    is_yelling = hey_bob.isupper()

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    elif is_question:
        return "Sure."
    elif is_yelling:
        return "Whoa, chill out!"

    return "Whatever."
