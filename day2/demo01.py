if __name__ == '__main__':
    m9=[1,2,3,4,5,6,7,8,9]
    for i in m9:
          for j in m9:
            print(str(i)+"*"+str(j)+"="+str(i*j).rjust(2),end="  ")
            if i==j:
                print()
                break
