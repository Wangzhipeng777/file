import random
if __name__ == '__main__':
      num=  input("请输入一个50-100的数字：")
      num1=  random.randint(50,100)
      if  int(num)>num1:
          print(num)
      else:
          print(num1)

      print(num)
      print(num1)