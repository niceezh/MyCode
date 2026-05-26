import functools

def total(basket):
    count = [0] * 5
    for book in basket:
        count[book - 1] += 1
    count_tuple = tuple(count)

    discount = {2: 5, 3: 10, 4: 20, 5: 25}

    @functools.lru_cache(maxsize=None)
    def min_cost(count_tuple):
        if all(c == 0 for c in count_tuple):
            return 0

        min_cost_value = float('inf')

        for s in range(5, 0, -1):
            from itertools import combinations
            books = [i for i in range(5) if count_tuple[i] > 0]
            if len(books) < s:
                continue

            for subset in combinations(books, s):

                new_count = list(count_tuple)
                for book_idx in subset:
                    new_count[book_idx] -= 1
                new_count_tuple = tuple(new_count)

                remaining_cost = min_cost(new_count_tuple)

                d = discount.get(s, 0)
                current_cost = s * 8 * (100 - d)

                total_cost = remaining_cost + current_cost
                if total_cost < min_cost_value:
                    min_cost_value = total_cost

        return min_cost_value

    return min_cost(count_tuple)


if __name__ == '__main__':
    print(total([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5]))
