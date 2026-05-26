def value(colors):
    if len(colors) < 2:
        return -1
    color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    color1, color2 = colors[0], colors[1]
    if color1 not in color_list or color2 not in color_list:
        return -1
    return color_list.index(color1) * 10 + color_list.index(color2)
