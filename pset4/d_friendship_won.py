def main():
    n = int(input())
    a = list(map(int, input().split()))

    l, r = 1, n
    ans = [float("inf"), None, None]
    sdv, sdm = a[l - 1], a[r - 1]
    while l < r:
        if abs(sdv - sdm) < ans[0]:
            ans = [abs(sdv - sdm), l, r]

        if sdv < sdm:
            l += 1
            sdv += a[l - 1]
        else:
            r -= 1
            sdm += a[r - 1]

    print(*ans)


if __name__ == '__main__':
    main()
