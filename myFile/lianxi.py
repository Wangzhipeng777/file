import os
import random
def xfile():
    """
    2.在1中的文件夹“exam-6”下创建一个python.txt文件，并依次向其中写入下述内容：（40分）
    1)Python的六大基本数据类型
    2)列举3个学过的Python模块，每个模块下各列举两个常用的方法
    """
    mfile = open(r"./exam-6/temp1.txt", "w")
    mfile.write("")
    mfile = open(r"./exam-6/temp2.txt", "w")
    mfile.write("")

def cfile():
    mfile=open(r"./exam-6/python.txt","w")
    mfile.write("Python的六大基本数据类型:\n"
                "number，string，list，tuple，sets,dictionary\n")
    mfile.write("2)列举3个学过的Python模块，每个模块下各列举两个常用的方法\n"
                "def fors(nlist):\n"
                "   for i in nlist\n"
                "       print(i)")
    """
    将1中创建的文档temp1.txt重命名为num.txt，
    并生成20个0到100之内的随机数，
    将这20个随机数写入num.txt文件，每行一个数。（40分）
    """
def mfile():
    cfile=open(r"./exam-6/temp1.txt","w")
    mlist=[random.randint(0,100) for i in range(0,10)]
    for i in mlist:
        cfile.writelines(str(i))
        cfile.writelines("\n")
def vfile():
    # 先获取当前工作目录
        ml = os.getcwd()
        print(ml)
        os.mkdir(ml+r"\exam-7")
        # os.mkdir(ml+r"\temp1.txt")
        # os.mkdir(ml + r"\temp2.txt")
        mfile = open(ml+r"\temp1.txt", "w")
        mfile.write("")
        mfile = open(ml+r"\temp2.txt", "w")
        mfile.write("")

if __name__ == '__main__':
    vfile()
