def intNumber(n: int, l=4):
    strNumber = str(n)
    tmp = l - len(strNumber)
    if tmp > 0:
        strNumber = '0'*tmp + strNumber
    return strNumber