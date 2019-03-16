if __name__ == '__main__':
    1.
    str=input("请输入一个字符串：")
    i=0
    myset=set()
    while i<str.__len__():
        c= str.count(str[i])
        #print(c)
        if c>1:
            myset.add(str[i])
        i += 1
    for j in myset:
        print(j)

    #2.
    str=input("请输入一个字符串：")
    myset=set(str)
    adict={}
    for i in myset:
        adict[i]  =  str.count(i)
    for i in myset:
        if adict[i]>=2:
            print(adict)
            break
    bdict= sorted(adict)

    for i in bdict:
        print("{0}:{1}".format(i,adict[i]),end=",")


    num1=input("请输入一个年份：")
    num=int(num1)
    if num%100==0 and num%400==0:
        print("这是闰年")
    elif num%100!=0 and num%4==0:
        print("这是闰年")
    else:
        print("这是平年")