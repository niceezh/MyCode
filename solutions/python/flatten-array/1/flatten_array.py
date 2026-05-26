def flatten(iterable):
    flattened = []
    for item in iterable:
        if isinstance(item, list):
            flattened.extend(flatten(item))
            continue
        if item != None:
            flattened.append(item)
    return flattened
