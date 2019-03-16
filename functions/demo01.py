if __name__ == '__main__':
    i = 0
    while i <= 6:
        j = 6 - i
        k = 0
        while j > 0:
            print(" ", end=" ")
            j -= 1
        while k < i:
            print("* "*i+" "*(6-i)+"* "*i, end=" ")
            break
        print()
        i += 1
    for j in range(12):
             print(" " * j, end="")
             print(" *" * (12 - j - 1), sep=" ")







