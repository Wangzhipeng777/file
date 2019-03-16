if __name__ == '__main__':
    str=[1,2,3,4,5]

   # index或许元素的下标值，从1开始
    for i in str:
       print("str[{0}]={1}".format(i.__index__(),i))


   # myid验证该lsit列表是否是重新创建的（或判断两个列表是否是同一个）
   # id 函数并不是list的独有函数    id相同为同一个对象，不同则不是
   # 切片复制不论如何切片都是重新创建的列表与原列表不同
    str1 = str[0:3]
    print("mlist id is {str}".format(str=id(str)))
    print("mlist id is {str1}".format(str1=id(str1)))
   # mlist id is 2568140579336
   # mlist id is 2568140579400

    #赋值产生的新列表与原列表的id是相同的
    str1=str
    print("mlist id is {str}".format(str=id(str)))
    print("mlist id is {str1}".format(str1=id(str1)))
   # mlist id is 1325355721224
   # mlist id is 1325355721224


