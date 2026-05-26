def resistor_label(colors):
    if len(colors) not in (1, 4, 5):
        return None

    if len(colors) == 1:
        return "0 ohms" if colors == ["black"] else None

    color_num = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
    color_tolerance = {"grey": "±0.05%", "violet": "±0.1%", "blue": "±0.25%", "green": "±0.5%", "brown": "±1%", "red": "±2%", "gold": "±5%", "silver": "±10%"}

    total_ohms = 0
    tolerance = ""

    if len(colors) == 4:
        if not set(colors[:3]).issubset(set(color_num.keys())) or colors[3] not in color_tolerance:
            return None
        total_ohms = (color_num[colors[0]] * 10 + color_num[colors[1]]) * (10 ** color_num[colors[2]])
        tolerance = color_tolerance[colors[3]]

    if len(colors) == 5:
        if not set(colors[:4]).issubset(set(color_num.keys())) or colors[4] not in color_tolerance:
            return None
        total_ohms = (color_num[colors[0]] * 100 + color_num[colors[1]] * 10 + color_num[colors[2]]) * (10 ** color_num[colors[3]])
        tolerance = color_tolerance[colors[4]]

    if not tolerance:
        return None

    units = [(10**9, "gigaohms"), (10**6, "megaohms"), (10**3, "kiloohms"), (1, "ohms")]
    for divisor, unit in units:
        if total_ohms >= divisor:
            value = total_ohms / divisor
            value = int(value) if value.is_integer() else value
            return f"{value} {unit} {tolerance}"

    return f"0 ohms {tolerance}"

