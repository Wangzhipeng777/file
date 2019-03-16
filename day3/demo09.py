# if __name__ == '__main__':
#     1.
#     mlist=[]
#     for i in range(1,11):
#         mlist.append(i)

    #2.
        #如果在list中既包含字符串，又包含其它类型数据，如何修改1中的生成式实现把一个list中所有的字符串变成小写？
        #（内建的isinstance(x, str)
       # 函数可以判断一个变量是不是字符串）
if __name__ == '__main__':
    L = ['Hello', 'World', 'IBM', 'Apple']
    l=[i.lower() for i in L ]
    print(l)
    L=['Hello', 'World', 12.5 ,'IBM', 'Apple', 6,True]
    l=[ i.lower() for i in L  if isinstance(i,str) ]
    print(l)




