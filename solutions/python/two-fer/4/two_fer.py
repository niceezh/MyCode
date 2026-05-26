def two_fer(name: str = 'you'):
    """Generate a two-fer sentence following the "one for X, one for me" format.
    
    Two-fer is a colloquial expression for "two for one", which means getting two items for the price of one.
    This function returns a formatted string that specifies who the extra item is for.

    Args:
        name (str, optional): The name of the person who receives the extra item. 
            Defaults to 'you' when no name is provided.

    Returns:
        str: A formatted two-fer sentence in the pattern "One for {name}, one for me.".
    """
    return f'One for {name}, one for me.'
