if __name__ == '__main__':
    n=  input("请输入一个数字：")
    n=int(n)
    m9=[1,2,3,4,5,6,7,8,9]
    for i in m9:
        if i <= n:
          for j in m9:
            print(str(i)+"*"+str(j)+"="+str(i*j),end=" ")
            if i==j:
                print()
                break
        else:
            break

        # name= input("you name: ")
        # print("{0} is {0}".format(name,"456","789"))