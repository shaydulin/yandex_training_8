def main():
    n = int(input())
    work_days = list(map(int, input().split()))

    mult = [0] * n
    sm = 0
    ans = 0
    for i, wd in enumerate(work_days):
        sm -= mult[i]
        ans += sm * wd
        if wd:
            if i + wd < n:
                mult[i + wd] += 1
            sm += 1
    print(ans)


if __name__ == '__main__':
    main()
