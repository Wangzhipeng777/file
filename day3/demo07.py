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
    mlist=[]
    mset=set()
    for k in klist:
        i=k.strip()
        mlist.append(i)
        mset.add(i)
    mdict={}
    for y in mset:
        mdict[y]=mlist.count(y)
    print(mdict)