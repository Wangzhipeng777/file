if __name__ == '__main__':
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]

    mset=set()
    nlist=list()
    mdict=dict()
    for i in klist:
        mset.add(i.strip())
        nlist.append(i.strip())
    for m in mset:
        c=nlist.count(m)
        if c>=2:
            mdict[m]=m
    print(mdict)


    mset=set({ i.strip() for i in klist})
    print(mset)
    mlist = list([i.strip() for i in klist])
    print(mlist)
    mdict=dict()
    for m in mset:
        c=mlist.count(m)
        if c >=2:
            mdict[m]=m

    print(mdict)