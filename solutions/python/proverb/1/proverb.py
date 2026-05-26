def proverb(*items, qualifier: str = ""):
    if not items:
        return []
    result = []
    for i in range(len(items) - 1):
        result.append(f'For want of a {items[i]} the {items[i+1]} was lost.')
    if qualifier:
        result.append(f'And all for the want of a {qualifier} {items[0]}.')
    else:
        result.append(f'And all for the want of a {items[0]}.')
    return result


if __name__ == "__main__":
    print(proverb("nail", "shoe", "horse", "rider", "message", "battle", "kingdom"))
