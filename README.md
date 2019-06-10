# qald
categorising QALD sentences into hard, medium and simple

# pos-complexity 
    if noun_count > 4 and other_count > 0:
        return pos_tagged_sentence, noun_count, "hard"

    elif (noun_count == 3 or noun_count==4) and other_count > 0:
        return pos_tagged_sentence, noun_count, "medium"

    else:
        return pos_tagged_sentence, noun_count, "easy"
# ner-complexity
    if entity_count >= 4:
        return words_ner, entity_count, "hard"
    elif entity_count == 3 or entity_count == 2:
        return words_ner, entity_count, "medium"
    else:
        return words_ner, entity_count, "easy"
