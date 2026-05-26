def response(hey_bob):
    hey_bob = str.strip(hey_bob)
    if hey_bob == "":
        return "Fine. Be that way!"
    if str.isupper(hey_bob):
        if hey_bob.endswith("?"):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if hey_bob.endswith("?"):
        return "Sure."
    return "Whatever."
