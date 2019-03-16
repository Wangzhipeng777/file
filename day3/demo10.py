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
    # mlist=[]
    # mset=set()
    # mdict={}
    # for i in klist:
    #     mlist.append(i.strip())
    #     mset.add(i.strip())
    # for l in mset:
    #     mdict[l]=l
    # print(mdict)


    mlist=[i.strip() for i in klist]
    mset=set(mlist)
    mdict={k : k for k in mset}
    print(mdict)




