if __name__ == "__main__":
    N = int(input())
    M = int(input())

    max_sum = N * (N + 1) // 2

    if M > max_sum:
        print("0")
    else:
        for i in range(N, 0, -1):
            if M <= i:
                print(M)
                M = 0
                break
            elif M > i:
                print(i)
                M -= i