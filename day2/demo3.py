import random
if __name__ == '__main__':
    #列表的创建 1
    mlist=list() #mlist=[]
    print(type(mlist))

    #列表的创建 2
    mlist=[]
    print(type(mlist))

    #添加到列表尾部
    mlist.append("123")
    print(mlist)

    #添加到指定位置
    mlist.insert(4,"456")
    print(mlist)

    #删除属性（默认删除最后一个）
    mlist.pop()
    print(mlist)

    #删除指定下标位置的元素
    del  mlist[0]

    #直接删除list对象，（参数可填list列表中的数值——指定数值删除）
    mlist.remove(参数)



    #mystu=["张学友","刘德华","郭德纲","李嘉诚"]
    mynum=[1,3,5,2,6,7,8]

    #保留列表本身，清空所有数据
    mynum.clear();

    #永久性排序，直接更改列表数值的顺序 reverse=True时为倒叙  默认为false
    mynum.sort(reverse=True)
    print(mynum)

    #打乱顺序，需要导入random包
    random.shuffle(mynum)
    print(mynum)

    #临时性排序  不会影响列表本身的排列顺序 reverse=True时为倒叙  默认为false
    #该函数是以返回值的方式给出一个新的排序后的列表
    mynum1 = []
    mynum1=sorted(mynum)
    print(mynum)
    print(mynum1)

    #以列表原有的顺序为基础的倒叙打印 永久性
    mynum.reverse()
    print(mynum)

    #列表拼接使用‘+’

    #列表的切片
    mynum1= mynum[0:3:2]
    print(mynum1)
    #格式：列表明[起始下标:结束下标:步长]
    #起始下标如果大于结束下标步长必须为负数
    #起始下标如果小于结束下标步长必须为正数

    #复制列表
    mynum1=mynum[:]
    print(mynum1)

    #列表常用函数
    #len():求列表函数
    # max():求列表中的最大值
    #     min():求列表中的最小值
    #     append():添加 默认添加到尾端
    #     insert():根据下标插入
    #     pop():删除，可以根据下标或值来删除
    #     remove():如果删除的值表中不存在会报错
    #             ：可以使用try except 语句处理程序出现的异常
    #             ：也可以实现判断被删除元素是否存在，然后再删除
    #     reversed():临时性排序，不会影响到原函数
    #     clear():清空列表中的值但保留列表对象
    #     extend():扩展，相当于两个列表相加的效果
    #     count:记录该字符串在另一个字符串中出现的次数
    #     copy：等同于  列表名1  = 列表名2[:]


