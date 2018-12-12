def datesSorting(obj, index=2):
    date = obj[index]
    return date[0] * 365 + date[1] * 31 + date[2]
