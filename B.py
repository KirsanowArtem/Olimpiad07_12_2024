if __name__ == "__main__":
    N = int(input())
    A = 1
    l=N-A
    if(N==2 or N==3):
        print("-1")
    elif(l%5==0):
        print((int)(l/5))
    elif (l % 5 == 1):
        print((int)(((l - 6) / 5) + 2))
    elif (l % 5 == 2):
        print((int)(((l-7) / 5)+2))
    elif (l % 5 == 3):
        print((int)(((l-3) / 5)+1))
    elif (l % 5 == 4):
        print((int)(((l - 4) / 5) + 1))