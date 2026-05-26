def color_code(color):
    color_list = colors()
    return color_list.index(color) if color in color_list else -1


def colors():
    return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

