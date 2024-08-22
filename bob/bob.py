def response(hey_bob):
    hey_bob = str(hey_bob).strip()
    is_question = hey_bob.endswith("?")
    is_yelling = hey_bob.isupper()

    if not hey_bob:
        return "Fine. Be that way!"
    elif is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    elif is_question:
        return "Sure."
    elif is_yelling:
        return "Whoa, chill out!"

    return "Whatever."
