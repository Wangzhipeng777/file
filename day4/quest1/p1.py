import random
def checkSex():

    name=input("请输入你的姓名：")
    sex=input("请输入你的性别：")
    try:
            mdict={"man":False,"boy":False,"男":False,"woman":True,"miss":True,"女":True}

            if mdict[sex]:
                print("{name}女士你好".format(name=name))
            else:
                print("{name}男士你好".format(name=name))
    except KeyError:
            print("请正确输入您的性别（如：男，女）")

def checkSet():
    nlist=[random.randint(1,100) for i in range(1,15)]
    mlist = [random.randint(1,100) for i in range(1, 15)]
    nset=set(nlist)
    mset=set(mlist)
    numset=nset | mset
    print(numset)


def checkEmail():
    Email=input("请输入你的邮箱：")
    if "@" not in Email:
        print("请输入正确的邮箱格式")
    mstr=str(Email).split("@")
    if mstr[0].__len__()<6:
        print("@符前至少6位")


def checkNum():
    num=input("请输入个数为奇数的数字：")
    if int(num)>2 and int(num)%2!=0:
        mlist=list(num)
        nlist=mlist[:]
        mlist.reverse()
        if nlist==mlist:
            print("是回文数")
        else:
            print("不是回文数")
    else:
        print("请输入个数为奇数的数字！")

