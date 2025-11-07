def main():
    n, m = map(int, input().split())
    table = []
    for _ in range(n):
        table.append(list(map(int, input().split())))

    h = sorted(
        ((i, j) for i in range(n) for j in range(m)),
        key=lambda coord: table[coord[0]][coord[1]]
    )

    mx_len = [[1] * m for _ in range(n)]

    difs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for i, j in h:
        for p, q in difs:
            i_, j_ = i + p, j + q

            if not 0 <= i_ < n or not 0 <= j_ < m:
                continue

            if table[i_][j_] - table[i][j] == 1:
                mx_len[i_][j_] = max(mx_len[i_][j_], mx_len[i][j] + 1)

        table[i][j] = -1

    print(max(max(row) for row in mx_len))


if __name__ == '__main__':
    main()
