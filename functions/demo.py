def sanjiao(x):
    i=0
    while i<=x:
        j = x-i
        k = 0
        while j>0:
            print(" ",end="")
            j-=1
        while k<i:
            print("*",end=" ")
            k+=1
        print()
        i+=1

def lingxing(num):
    for i in range(0,num):
        print(" "*(num-i),end=" ")
        print("  *"*i,sep="  ")
    for i in range(0,num):
        print("  " * i,end=" ")
        print(" ",end="")
        print("*  "*(num-i))
def duiqi(num):
    for i in range(0,num):
        if i%10==0:
            pass

def ling(x):
    i = 0
    while i < x:
        j = x - i
        k = 0
        while j > 0:
            print(" ", end="")
            j -= 1
        while k < i:
            print("*", end=" ")
            k += 1
        print()
        i += 1
    m = 0
    while m < x:
        j = 0
        k = x - m
        while j < m:
            print(" ", end="")
            j += 1
        while k > 0:
            print("*", end=" ")
            k -= 1
        print()
        m += 1
def shuzi(num):
    for i in range(num+1):
        if i % 10 == 0:
            print("")
        print(str(i).center(4),end="")

def chefa(num):
        for i in range(1,num):
            for l in range(1, num):
                print("{0}*{1}={2}   ".format(l, i, (l * i)),end="")
                if i == l:
                    print("")
                    break

if __name__ == '__main__':
    # lingxing(5)

        num=6
        for i in range(num + 1):
            print(" " * (num - i + 1), end="")
            print(" *" * i, sep=" ")
        for j in range(num):
            print(" " * (j + 2), end="")
            print(" *" * (num - j - 1), sep=" ")

if __name__ == '__main__':
    s = int(input("请输入一个数："))
    for i in range(s + 1):
        print(" " * (s - i), end=" ")
        print(" *" * i, sep=" ")
    s = s - 1
    for i in range(s):
        print(" " * i, end="  ")
        print(" *" * (s - i), sep=" ")

if __name__ == '__main__':

    chefa(10)








    rows=input("请输入一个数值：")

    for i in range(0, rows + 1):  # 变量i控制行数
        for j in range(0, rows - i):  # (1,rows-i)
            print
            " ",
            j += 1
        for k in range(0, 2 * i - 1):  # (1,2*i)
            if k == 0 or k == 2 * i - 2 or i == rows:
                if i == rows:
                    if k % 2 == 0:  # 因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                        print("*")

                    else:
                        print("*")
                          # 注意这里的","，一定不能省略，可以起到不换行的作用
                else:
                    print("*")

            else:
                print("")

            k += 1
        print("/n")

        i += 1
    rows=input("请输入一个数值：")

    for i in range(0, rows + 1):  # 变量i控制行数
        for j in range(0, rows - i):  # (1,rows-i)
            print
            " ",
            j += 1
        for k in range(0, 2 * i - 1):  # (1,2*i)
            if k == 0 or k == 2 * i - 2 or i == rows:
                if i == rows:
                    if k % 2 == 0:  # 因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                        print("*")

                    else:
                        print("*")
                          # 注意这里的","，一定不能省略，可以起到不换行的作用
                else:
                    print("*")

            else:
                print("")

            k += 1
        print("/n")

        i += 1
    rows=input("请输入一个数值：")

    for i in range(0, rows + 1):  # 变量i控制行数
        for j in range(0, rows - i):  # (1,rows-i)
            print
            " ",
            j += 1
        for k in range(0, 2 * i - 1):  # (1,2*i)
            if k == 0 or k == 2 * i - 2 or i == rows:
                if i == rows:
                    if k % 2 == 0:  # 因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                        print("*")

                    else:
                        print("*")
                          # 注意这里的","，一定不能省略，可以起到不换行的作用
                else:
                    print("*")

            else:
                print("")

            k += 1
        print("/n")

        i += 1
    rows=input("请输入一个数值：")

    for i in range(0, rows + 1):  # 变量i控制行数
        for j in range(0, rows - i):  # (1,rows-i)
            print
            " ",
            j += 1
        for k in range(0, 2 * i - 1):  # (1,2*i)
            if k == 0 or k == 2 * i - 2 or i == rows:
                if i == rows:
                    if k % 2 == 0:  # 因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                        print("*")

                    else:
                        print("*")
                          # 注意这里的","，一定不能省略，可以起到不换行的作用
                else:
                    print("*")

            else:
                print("")

            k += 1
        print("/n")

        i += 1
    rows=input("请输入一个数值：")

    for i in range(0, rows + 1):  # 变量i控制行数
        for j in range(0, rows - i):  # (1,rows-i)
            print
            " ",
            j += 1
        for k in range(0, 2 * i - 1):  # (1,2*i)
            if k == 0 or k == 2 * i - 2 or i == rows:
                if i == rows:
                    if k % 2 == 0:  # 因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                        print("*")

                    else:
                        print("*")
                          # 注意这里的","，一定不能省略，可以起到不换行的作用
                else:
                    print("*")

            else:
                print("")

            k += 1
        print("/n")

        i += 1