import random
if __name__ == '__main__':
    pass
    #python的很多基本函数的用法都与java一致，但是语法却有很大的不同。
    #  1.循环或判断语句不可以写在小括号内
    #  2.判断语句后用‘：’ 后表示循环体
    #  3.结束语句初不用‘；’
    #  4.循环体或判断语句后需要缩进一个tab




    #1.
    #补充空行，当循环体或判断后所执行的代码不需要写的时候
    # 用pass表示该行代码为空。如果没有pass编译错误
    #   for i in [1,2,3,4]:
    #        pass

    #2.
    #  while 循环所实现的功能与java一致，需要注意的是语法格式
    # i=0
    #  while i>10:
    #        i+=1

    #3.
    #  if 语句；语法格式与循环一致。需注意的是 else if  语句 为 elif
    # i=-5
    # if i>0:
    #     print("123")
    # elif i==3:
    #     print(7)

    #4.
    # 字符串切片 第一个参数为开始数字（包含）。第二个参数为结束数字（不包含）。第三个参数为步长变化（选填）
    # str=" u can u bb,no bb bb  "
    # print(str[0:10:3])

    #5.
    #将字符串中的所有字母转换为大写
    # str = " u can u bb,no bb bb  "
    # print(str.upper())

    # 将字符串中的所有字母转换为小写
    # str=" U CAN U BB,NO BB BB   "
    # print(str.lower())

    # 将字符串中的所有单词的首个字符转换为大写
    #  str=" u can u bb,no bb bb   "
    #  print(str.title())

    #6.
    # name="hh"
    # age=18
    # sex="man"

    #正常输出
    #print(name,age,sex)

    #修改字符串结尾字符，清除自动换行
    #print(name,age,sex,end="")
    #print(name, age, sex, end="")

    #修改输出参数的间隔符号（默认为空格）
    #print(name,age,sex,sep="-")

    #7.
    #输入字符
    # var=  input("请输入一个字符：")
    # print(var)

    #8.
    #使用指定变量输出指定值，（键值对的形式）
    # var="123"
    # print("var={var}".format(var=var))