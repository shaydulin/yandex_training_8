from itertools import groupby


def main():
    n, m = map(int, input().split())
    mat = []
    for _ in range(n):
        mat.append([1 if ch == "X" else (-1 if ch == "O" else 0) for ch in input()])

    if check(mat, n, m):
        print("Yes")
        return

    mat = [*zip(*mat)]
    mat.reverse()
    if check(mat, m, n):
        print("Yes")
        return

    print("No")


def check(mat, n, m):
    if any(
        k != 0 and sum(1 for _ in g) >= 5 for k, g in groupby(mat[0])
    ):
        return True

    prev_row = [1] * m
    for i in range(1, n):
        if any(
            k != 0 and sum(1 for _ in g) >= 5 for k, g in groupby(mat[i])
        ):
            return True
        cur_row = [1] * m
        for j in range(1, m):
            if mat[i][j] == mat[i - 1][j - 1] != 0:
                cur_row[j] += prev_row[j - 1]
                if cur_row[j] >= 5:
                    return True
        prev_row = cur_row

    return False


if __name__ == '__main__':
    main()
