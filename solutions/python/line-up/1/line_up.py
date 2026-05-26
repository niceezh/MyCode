def line_up(name, number):
    return f'{name}, you are the {number}{get_suffix(number)} customer we serve today. Thank you!'


def get_suffix(number):
    last_one = number % 10
    last_two = number % 100
    if last_one == 1 and last_two != 11:
        return 'st'
    if last_one == 2 and last_two != 12:
        return 'nd'
    if last_one == 3 and last_two != 13:
        return 'rd'
    return 'th'

