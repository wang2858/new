lis = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12,
       'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24,
       'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35}
li = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def dq(num, news, new):
    tt = 0
    num = str(num)
    num = da(num, news)
    if new < 10:
        while num >= new:
            tt += ds(num, new)[0]
            num -= new ** (ds(num, new)[1] - 1)
        print(tt)
    else:
        dx(num, new)


def dx(n=100, c=2):  # 大于10的转化
    ttt = 0
    d = []
    while 1:
        if c ** ttt > n:
            for i in range(1, ttt + 1):
                dd = 0
                while dd * c ** (ttt - i) <= n:
                    dd += 1
                if n < c ** (ttt - i):
                    if n < c ** (ttt - (i + 1)):
                        dd = n + 1
                    else:
                        dd = 1
                elif dd == 0:
                    dd = 1
                else:
                    n -= (dd - 1) * c ** (ttt - i)
                print(li[dd - 1], end='')  # 不要删
            break
        elif n >= c ** ttt:
            ttt += 1
    return d


def ds(n=100, new=0):
    daa = 0
    while n >= new:
        if n < new ** daa:
            break
        daa += 1
    return 10 ** (daa - 1), daa


def da(q='100', t=36):  # 转化成10
    data = 0
    ttt = 0
    for i in q:
        data -= 1
        ttt = ttt + lis[f"{i}"] * t ** (data + len(q))
    return ttt


dq('300', 32, 18)
