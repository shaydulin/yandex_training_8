def main():
    n, m = map(int, input().split())
    mapping = {
        "+": 1,
        "-": -1,
        "?": 0,
    }
    mat = []
    sum_rows = []
    zeros_rows = []
    for _ in range(n):
        row = [mapping[ch] for ch in input()]
        mat.append(row)
        sum_rows.append(sum(row))
        zeros_rows.append(row.count(0))
    sum_cols = []
    zeros_cols = []
    for col in zip(*mat):
        sum_cols.append(sum(col))
        zeros_cols.append(col.count(0))

    ans = float("-inf")
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                ans = max(ans, sum_rows[i]  - sum_cols[j] + zeros_rows[i] + zeros_cols[j] - 2)
            else:
                ans = max(ans, sum_rows[i]  - sum_cols[j] + zeros_rows[i] + zeros_cols[j])

    print(ans)


if __name__ == '__main__':
    main()
