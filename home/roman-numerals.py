def checkio(data):

    s = ""
    l = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    v = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    for letter, value in zip(l, v):
        s += letter*(data//value)
        data %= value

    return s

if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
