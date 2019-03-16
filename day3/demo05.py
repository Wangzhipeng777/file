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
    #创建set集合和list集合
    #将去过空格的list集合放入新建的集合中
    #将去完空格的数据放入set集合中去重
    mset = set()
    mlist=list()
    for i in klist:
        i = i.lstrip()
        i = i.rstrip()
        mlist.append(i)
        mset.add(i)
    mdict={}
    #遍历set集合中去重后的数据进行词频计算
    for l in mset:
        print(l)
        mdict[l]=mlist.count(l)

    print(mdict)