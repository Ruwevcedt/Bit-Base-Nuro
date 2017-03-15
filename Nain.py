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
        s = bl2
    else:
        s = bl1
    for count in range(s):
        o.append(andbb_b(blst1[count], blst2[count]))
    return o


def pushblis_bl(blst, isqr):
    o = []
    il = len(isqr)
    for lp1 in range(il):
        tl = []
        for lp2 in isqr[lp1]:
            tl.append(blst[lp2])
        o.append(resiznbl_bl(1, tl)[0])
    return o


def sumblbl_il(blst1, blst2):
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


def sumaxxbs_bl(bsqr):
    ot = []
    oa = []
    for bsc in bsqr:
        ot = sumblbl_il(ot, bsc)
        oa = sumblbl_il(oa, [1] * len(bsc))
    oc = len(oa)
    o = []
    for count in range(oc):
        fot = float(ot[count])
        foa = float(oa[count])
        if fot / foa >= 0.5:
            o.append(True)
        else:
            o.append(False)
    return o


def resiznbl_bl(n, blst):
    bl = len(blst)
    fbl = float(bl)/2

    if n == bl:
        return blst
    elif n == 1:
        t = 0.0
        for lp1 in blst:
            t += lp1
        if t >= fbl:
            return [True]
        else:
            return [False]

    fn = float(n)
    o = []
    lt = []
    ft = float(True)
    ff = float(False)
    fw = fbl/fn
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
