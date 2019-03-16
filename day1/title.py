if __name__ == '__main__':
    #mstr=" u can u uo  "
    #每个单词的首字母大写
    #print(mstr.title())

    #type
    #输出字符类型
    #print(type(mstr))


    uname = "张三"
    upassword="hehe"
    usex="man"

    #默认print的使用方式
    print(uname,upassword,usex)

    #替换结尾换行或给结尾增加输出字符，用end参数实现
    print(uname,upassword,usex,end="??   ")

    #替换参数之间的分隔符，使用sep参数实现
    print(uname,upassword,usex,sep="-")