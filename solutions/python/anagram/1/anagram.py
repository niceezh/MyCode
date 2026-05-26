def find_anagrams(word, candidates):
    word_upper = word.upper()
    res = []
    for candidate in candidates:
        candidate_upper = candidate.upper()
        if candidate_upper != word_upper and sorted(candidate_upper) == sorted(word_upper):
            res.append(candidate)
    return res
