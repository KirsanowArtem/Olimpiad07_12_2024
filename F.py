if __name__ == "__main__":
    N = int(input())
    A, B = map(int, input().split())

    AA = A
    BB = B
    while BB != 0:
        AA2 = BB
        BB = AA % BB
        AA = AA2

    min2 = (A * B) // AA
    A2 = N // A
    B2 = N // B
    AB2 = N // min2

    print(A2 + B2 - AB2)
