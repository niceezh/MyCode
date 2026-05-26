def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot_sum = sum(i for i in range(1, number // 2 + 1) if number % i == 0)
    if number < aliquot_sum:
        return "abundant"
    if number > aliquot_sum:
        return "deficient"
    return "perfect"
