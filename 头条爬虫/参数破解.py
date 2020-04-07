def toHex(num):
    """
    :type num: int
    :rtype: str
    """
    chaDic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    hexStr = ""
    if num < 0:
        num = num + 2 ** 32
    while num >= 16:
        digit = num % 16
        hexStr = chaDic.get(digit, str(digit)) + hexStr
        num //= 16
    hexStr = chaDic.get(num, str(num)) + hexStr
    return hexStr


def get_sign():
    import time
    import hashlib
    e = int(int(time.time())*1000 / 1e3)
    i = toHex(e).upper()
    hash = hashlib.md5()
    t1 = hash.update(bytes(i,encoding='utf-8'))
    t = str(hash.hexdigest()).upper()
    if len(i) != 8:
        return {'as': "479BB4B7254C150",'cp': "7E0AC8874BB0985"}
    o = t[0:5]
    n = t[-5:]
    a = ''
    r = ''
    for s in range(5):
        a = a + o[s] + i[s]
        r = r + i[s+3] + n[s]
    return {'as': "A1" + a + i[-3:],'cp': i[0:3] + r + "E1"}
print(get_sign())
