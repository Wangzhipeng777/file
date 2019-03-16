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
    for i in klist:
        mset.add(i.strip())
        nlist.append(i.strip())
    for l in mset:
        if nlist.count(l)>=2:
            print(l)

