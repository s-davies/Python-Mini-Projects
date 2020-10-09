def parse(string):
    d = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    res = 0
    i = 1
    while i < len(string):
        if d[string[i-1]] < d[string[i]]:
            res += d[string[i]] - d[string[i-1]]
            i += 2
        else:
            res += d[string[i-1]]
            i += 1
    if i == len(string):
        res += d[string[i-1]]
    return res
