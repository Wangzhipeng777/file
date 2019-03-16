if __name__ == '__main__':
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " sup",
        " day ", "day", " up",
    ]
    str=""
    mlist=[]
    for k in klist:
        str+=k.strip()
    mlist.append(str)
    mdict={}
    str2="goodgoodstudy"
    mdict["goodgoodstudy"]=mlist.count(str2)
    print(mlist)
    print(mdict)