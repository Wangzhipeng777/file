def reverse():
    str=input("请输入字符串：")
    mlist=list(str)
    mlist.reverse()
    mstr=""
    for i in mlist:
        mstr+=i
    print("{mstr}的格式为".format(mstr=mstr),end="")
    print(type(mstr))
"""
创建一个列表，存储公司10个名单，
对这些名单进行排序，要求按姓名的字符多少来排。（30分）
"""
def sort():

    nlist=list()
    l=0
    for i in range(1,11):
        names=input("请输入第{i}个人的名字：".format(i=i))
        nlist.append(names)
    c=""
    mdict={}
    alist = list()
    blist = list()
    clist = list()
    dlist = list()
    print(nlist)
    for i in nlist:
        if i.__len__()==1:
            alist.append(i)
        if i.__len__()==2:
            blist.append(i)
        if i.__len__()==3:
            clist.append(i)
        if i.__len__()==4:

            dlist.append(i)
    mdict[1] = alist
    mdict[2] = blist
    mdict[3] = clist
    mdict[4] = dlist

    str=""
    print(mdict)
    for i in mdict.values():
        for l in i:
         print(l)

        """
        输入用户名密码进行注册，要求用户名允许数字字母6-16位，
        密码6-16位，不允许出现*#!（30分）
        """
def regist():
    user=input("请输入用户名:")
    pwd=input("请输入密码：")

    if user.isalnum() and user.__len__()>=6 and user.__len__()<=16:
        print("用户名可以使用")
    else:
        print("用户名只允许数字字母，并且是6-16位")

    if "*" not in pwd and "#" not  in pwd and "!" not in pwd \
            and pwd.__len__() >= 6 and pwd.__len__() <= 16:
        print("密码可以使用")
    else:
        print("密码6-16位，不允许出现*#!")



# def sss():
#     mlist = ["张震", "王越", "靳中伟", "李庸", "李广军"]
#
#     nlist = [len(m) for m in mlist]
#
#     i = 0
#
#     while i < 5:
#
#         j = 0
#
#         while j < 4:
#
#             if int(nlist[j]) < int(nlist[j + 1]):
#                 i = nlist[j]
#
#                 nlist[j] = nlist[j + 1]
#
#                 nlist[j + 1] = i
#
#                 i1 = mlist[j]
#
#                 mlist[j] = mlist[j + 1]
#
#                 mlist[j + 1] = i1
#
#             j = j + 1
#
#         i = i + 1
#         print(mlist)


"""
输入一个字符串为社会主义核心价值观的全拼，
每个词用空格进行分隔，将这个字符串，转成列表，遍历输出
"""
def ylist():
    str="she hui zhu yi he xin jia zhi guan"
    mlist=str.split(" ")
    print(mlist,end="")
