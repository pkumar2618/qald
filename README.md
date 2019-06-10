# qald
categorising QALD sentences into hard, medium and simple

# pos-complexity 
    if noun_count > 3 and other_count > 0:
        return "hard"
    elif noun_count == 3 and other_count > 0:
        return "medium"
    else:
        return "easy"

# ner-complexity
    if entity_count >= 5:
        return "hard"
    elif entity_count == 4:
        return "medium"
    else:
        return "easy"

