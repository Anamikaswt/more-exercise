def break_into_words(sentence):
    sign=" "
    result=[]
    word=" "
    for a in sentence:
        if a not in sign:
            word+=a
        elif word:
            result.append(word)
            word=" "
    if word:
        result.append(word)
    result.append(word)
    return result
b=break_into_words("NavGurukul is an alternative to higher education reducing the barriers of current formal education system" )
print(b)