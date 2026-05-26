def recite(start_verse, end_verse):
    animals = [
        ("fly", ""),
        ("spider", "It wriggled and jiggled and tickled inside her."),
        ("bird", "How absurd to swallow a bird!"),
        ("cat", "Imagine that, to swallow a cat!"),
        ("dog", "What a hog, to swallow a dog!"),
        ("goat", "Just opened her throat and swallowed a goat!"),
        ("cow", "I don't know how she swallowed a cow!"),
        ("horse", "She's dead, of course!")
    ]
    verses = []
    for i in range(start_verse-1, end_verse):
        animal, desc = animals[i]
        verses.append(f'I know an old lady who swallowed a {animal}.')
        if desc:
            verses.append(desc)
        if i == 7:
            break
        for j in range(i, 0, -1):
            cur_animal = animals[j][0]
            pre_animal = animals[j-1][0]
            if j == 2:
                verses.append(f'She swallowed the {cur_animal} to catch the {pre_animal} that wriggled and jiggled and tickled inside her.')
            else:
                verses.append(f'She swallowed the {cur_animal} to catch the {pre_animal}.')
        verses.append("I don't know why she swallowed the fly. Perhaps she'll die.")
        if i != end_verse-1:
            verses.append('')
    return verses

if __name__ == '__main__':
    for verse in recite(1, 8):
        print(verse)
