def sum_of_multiples(limit, multiples):
    set_list = []
    for multiple in multiples:
        if multiple:
            set_list.append(set(num for num in range(1, limit) if num % multiple == 0))
    if not set_list:
        return 0
    return sum(set.union(*set_list))
