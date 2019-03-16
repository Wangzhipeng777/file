if __name__ == '__main__':
    dete=input("请输入年月日：")
    time=dete[0:4]
    M=dete[4:6]
    date=dete[6:8]
    i=1
    num=0
    m=int(M)+1
    time=int(time)
    while i>m:
        if i==1:
            num+=0
        if  i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
            num+=i*31
        if i==4 or i==6 or i==9 or i==11:
            num+=i*30
        if i==2:
            if (time%4==0 and time%100!=0) or (time%400==0):
                num+=i*29
            else:
                num+=i*28
        i+=1
    print("这是{timeK}年的第{dateK}天".format(timeK=time,dateK=num))