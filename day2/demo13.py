if __name__ == '__main__':
    str=input("请输入一个字符串：")
    mdict={}
    for i in str:
        mdict[i]=str.count(i)

    for k in str:
        if mdict[k]>=2:
            print(k)
            break
    adict=sorted(mdict)

    for l in adict:
        print("mdictK={0},mdictV={1}".format(l,mdict[l]))