import random
if __name__ == '__main__':

    #菱形
    num=[1,2,3,4,5]
    num1=[4,3,2,1]
    for i in num:
        print("  " * (5 - i), end="")
        print(" *  " * (i))
    for j in num1:
        print("  " * (5-j),end="")
        print(" *  " * (j))

