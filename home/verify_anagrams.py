def verify_anagrams(first_word, second_word):
    r = list(first_word.replace(" ", "").lower())
    d = list(second_word.replace(" ", "").lower())
    pos = 0
    matched = True
    r.sort()
    d.sort()
    if len(r) != len(d):
        return False
    while pos < len(r) and matched:
        if r[pos] == d[pos]:
            pos += 1
        else:
            matched = False

    return matched


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"