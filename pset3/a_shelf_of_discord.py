def main():
    a, b, s = map(int, input().split())
    l = max(a, b)
    r = s + max(a, b) + 1
    while l < r:
        m = (l + r) // 2
        s_ = (m - a) * (m - b)
        if s_ < s:
            l = m + 1
        elif s_ > s:
            r = m
        else:
            print(m)
            return
    print(-1)


if __name__ == '__main__':
    main()
