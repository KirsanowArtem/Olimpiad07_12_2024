if __name__ == "__main__":
    N = int(input())
    mass = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    for size in range(1, N):
        for i in range(N - size):
            for j in range(N - size):
                l1 = mass[i][j]
                l2 = mass[i][j + size]
                l3 = mass[i + size][j]
                l4 = mass[i + size][j + size]

                if l1 == l2 == l3 == l4:
                    count += 1

    for xt1 in range(N):
        for yt1 in range(N):
            for xt2 in range(xt1 + 1, N):
                for yt2 in range(yt1 + 1, N):
                    t1 = (xt1, yt1)
                    t2 = (xt2, yt2)

                    dx, dy = xt2 - xt1, yt2 - yt1
                    t3 = (xt1 - dy, yt1 + dx)
                    t4 = (xt2 - dy, yt2 + dx)

                    if 0 <= t3[0] < N and 0 <= t3[1] < N and 0 <= t4[0] < N and 0 <= t4[1] < N:
                        if mass[t1[0]][t1[1]] == mass[t2[0]][t2[1]] == mass[t3[0]][t3[1]] == mass[t4[0]][t4[1]]:
                            count += 1

    print (count)