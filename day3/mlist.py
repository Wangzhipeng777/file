if __name__ == '__main__':
    mlist = list()
    print(type(mlist))

    mlist.append("+1")
    print(mlist)

    mlist.insert(0,"-1")
    print(mlist)

    mlist.remove("-1")
    print(mlist)

    mlist.pop()
    print(mlist)

    mset={1,2,3,4,5,10}
    mset.discard(10)
    print(mset)

    