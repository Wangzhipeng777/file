import day4.quest1.p1 as pp
if __name__ == '__main__':
   while True:
        mset={
            1:"输入用户姓名及性别，然后给出提示",
            2:"随机生成两个整数的列表，并计算输出两个列表的并集",
            3:"注意一个用户信息,姓名长度不能少于6位，邮件中包含@",
            4:"从键盘输入一行字符串，判断是否是回文数",
            0:"退出"
        }
        print("\n\n")
        #
        for i in mset.items():
             print(i)
        elm=input("请输入服务项目:")
        elm=int(elm)
        # if elm==1:
        #     pp.checkSex()
        # if elm==2:
        #     pp.checkSet()
        # if elm==3:
        #     emal=input("请输入您的邮箱地址：")
        #     pp.checkEmail(emal)
        # if elm==4:
        #     num=input("请输入一串数字（注意数字个数为大于1的奇数个数）:")
        #     pp.checkNum(num)
        # if elm==0:
        #     print("正在退出.....")
        #     break
        nset={
            1:pp.checkSex,
            2:pp.checkSet,
            3:pp.checkEmail,
            4:pp.checkNum,
        }


        for i in mset.keys():
            if i == elm:
                nset[elm]()