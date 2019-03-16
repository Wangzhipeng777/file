if __name__ == '__main__':
    mlist = ["李墉","王春旺","王越","史偏颇盘"]
    for i in range(4):
        mlist.append(input("请输入名字："))
    print(mlist)
    nlist = [len(i) for i in mlist]
    print(nlist)
    glist = []
    a = 0
    i=0
    while i < len(nlist) :
        if nlist[i] >= a :
            a = nlist[i]
            glist.insert(0,mlist[i])
        else :
            glist.append(mlist[i])
        i+=1
    print(glist)