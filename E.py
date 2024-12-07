if __name__ == "__main__":
    N = int(input())
    num = list(map(int, input().split()))
    num.sort()

    for i in range(N):
        if i == 0:
            if num[i] != num[i + 1]:
                print(num[i])
                break
        elif i == N - 1:
            if num[i] != num[i - 1]:
                print(num[i])
                break
        else:
            if num[i] != num[i - 1] and num[i] != num[i + 1]:
                print(num[i])
                break
    else:
        print("-1")