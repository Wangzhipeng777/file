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
    mdict=dict()
    nlist=[]
    for i in klist:
        mset.add(i.strip())
        nlist.append(i.strip())
    for l in mset:
        c = nlist.count(l)
        if c>=2:
            mdict[l]=c
    print(mdict)