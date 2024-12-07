if __name__ == "__main__":
    N = int(input())
    K = int(input())

    if K % 2 == 1:
        print ((K + 1) // 2)
    else:
        print ((K // 2) + (N + 1) // 2)