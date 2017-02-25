def andbb_b(b1, b2):
    return b1 == b2


def andbbl_bl(b, blst):
    o = []
    bl = len(blst)
    for count in range(bl):
        o.append(andbb_b(b, blst[count]))
    return o


def andblbl_bl(blst1, blst2):
    o = []
    bl1 = len(blst1)
    bl2 = len(blst2)
    if bl1 >= bl2:
        l = bl2
    else:
        l = bl1
    for count in range(l):
        o.append(andbb_b(blst1[count], blst2[count]))
    return o


def andbsbl_bs(bsqr, blst):
    o = [[]]
    for sc in bsqr:
        o.append(andblbl_bl(sc, blst))
    return o


def sumbbl_bl(b, blst):
    o = []
    for blc in blst:
        o.append(b + blc)
    return o


def sumblbl_bl(blst1, blst2):
    o = []
    bl1 = len(blst1)
    bl2 = len(blst2)
    if bl1 >= bl2:
        llong = list(blst1)
        lshort = list(blst2)
        longer = bl1
        shorter = bl2
    else:
        llong = list(blst2)
        lshort = list(blst1)
        longer = bl2
        shorter = bl1
    for count in range(0, shorter, 1):
        o.append(llong[count] + lshort[count])
    for count in range(shorter, longer, 1):
        o.append(0 + llong[count])
    return o


def sumaxxbs_il(bsqr):
    o = []
    for bsc in bsqr:
        o = sumblbl_bl(o, bsc)
    return o


def resiznbl_bl(n, blst):
    bl = len(blst)
    fbl = float(bl)
    fn = float(n)

    if n == bl:
        return blst

    o = []
    lt = []
    ft = float(True)
    ff = float(False)
    fw = fbl/(2*fn)
    for lp1 in range(bl):
        if blst[lp1]:
            t = ft/fn
        else:
            t = ff
        for lp2 in range(n):
            lt.append(t)
    c = 0
    t = 0.0
    for lp1 in range(n):
        for lp2 in range(bl):
            t += lt[c]
            c += 1
        if t >= fw:
            o.append(True)
        else:
            o.append(False)
        t = 0.0
    return o


def resiznbs_bs(n, bsqr):
    o = [[]]
    for bsc in bsqr:
        o.append(resiznbl_bl(n, bsc))
    return o
