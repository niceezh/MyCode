def recite(start_verse, end_verse):
    if not 1 <= start_verse <= end_verse <= 12:
        raise ValueError("Invalid verse")
    
    prefix = "This is"
    roles = ["", " the malt", " the rat", " the cat", " the dog", " the cow with the crumpled horn", " the maiden all forlorn", " the man all tattered and torn", " the priest all shaven and shorn", " the rooster that crowed in the morn", " the farmer sowing his corn", " the horse and the hound and the horn"]
    actions = [" the house that Jack built", " that lay in", " that ate the malt", " that killed the rat", " that worried the cat", " that tossed the dog", " that milked the cow with the crumpled horn", " that kissed the maiden all forlorn", " that married the man all tattered and torn", " that woke the priest all shaven and shorn", " that kept the rooster that crowed in the morn", " that belonged to the farmer sowing his corn"]

    sentance = prefix + roles[start_verse - 1]
    for i in range(start_verse, 0, -1):
        sentance += actions[i - 1]
    sentance += "."

    if start_verse == end_verse:
        return [sentance]
    else:
        return [sentance] + recite(start_verse + 1, end_verse)
