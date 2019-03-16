import day4.quset2.mfcution as dd

if __name__ == '__main__':

    while True:

        print("1.对一字符串进行翻转操作。")
        print("2.创建一个列表，存储公司10个名单，对这些名单进行排序，要求按姓名的字符多少来排。")
        print("3.输入用户名密码进行注册，要求用户名允许数字字母6-16位，密码6-16位，不允许出现*#!")
        print("4.输入一个字符串为社会主义核心价值观的全拼，"\
              "每个词用空格进行分隔，将这个字符串，转成列表，遍历输出")
        print("0.退出")
        elm=input("请选择服务项目：")
        mdict={
        1:dd.regist,
        2:dd.sort,
        3:dd.regist,
        4:dd.ylist
        }


        """
        if __name__ == '__main__':
        reverse()
        sort()
        regist()
        ylist()
        
        """
        elm=int(elm)
        if elm==0:
            print("正在退出........")
            break
        for i in mdict.keys():
            if elm==i:
                mdict[elm]()
