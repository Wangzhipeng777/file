if __name__ == '__main__':
    #myset=set("  aabbcctr  ")
     #for i in myset:
         #print(i)


    mset=set({"1","2","3","4","5"})
    nset=set({"4","5","6","7","8"})
    a=    mset.difference(nset)
    print(a)

    b=mset.intersection(nset)
    print(b)

    c=mset.union(nset)
    print(c)

    d=mset.issubset(nset)
    print(d)

    e=mset.issuperset(nset)
    print(e)

    f=mset-nset
    print(f)
