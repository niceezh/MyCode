def label(colors):
    if len(colors) < 3:
        return None
    color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    color1, color2, color3 = colors[0], colors[1], colors[2]
    if color1 not in color_list or color2 not in color_list or color3 not in color_list:
        return None
    total_ohms = (color_list.index(color1) * 10 + color_list.index(color2)) * (10 ** color_list.index(color3))
    units = [(10**9, "gigaohms"), (10**6, "megaohms"), (10**3, "kiloohms"), (1, "ohms")]
    for divisor, unit in units:
        if total_ohms >= divisor:
            value = total_ohms / divisor
            value = int(value) if value.is_integer() else value
            return f'{value} {unit}'
    return "0 ohms"
