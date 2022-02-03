def list_reverse(words: list):
    chained_reversed = ''.join(words)[::-1]
    list_reversed = []
    it = 0
    for word in words:
        list_reversed.append(chained_reversed[it: it + len(word)])
        it += len(word)
    return list_reversed
