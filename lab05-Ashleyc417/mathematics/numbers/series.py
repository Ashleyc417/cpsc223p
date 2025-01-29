def sum(list):
    s = 0
    for i in list:
        s += i
    return s

def average(list):
    avg = sum(list)
    avg = avg / len(list)
    return avg
