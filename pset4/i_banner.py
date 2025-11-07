def main():
    n, d = map(int, input().split())
    trees = []
    for _ in range(n):
        trees.append(tuple(map(int, input().split())))
    trees = set(trees)


    ans = 0
    difs = get_difs(d)
    for x, y in trees:
        for p, q in difs:
            ans += int((x + p, y + q) in trees)

    print(ans)


def get_difs(d):
    coord = [*range(int(d**.5) + 1)]
    j = len(coord) - 1
    difs = []
    for i in coord:
        while coord[i]**2 + coord[j]**2 > d:
            j -= 1

        if coord[i]**2 + coord[j]**2 == d:
            if coord[i]:
                difs.append((coord[i], coord[j]))
            if coord[j]:
                difs.append((coord[i], -coord[j]))

    return difs


if __name__ == '__main__':
    main()
