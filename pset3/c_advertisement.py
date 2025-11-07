def main():
    n, w, h = map(int, input().split())
    words = []
    for _ in range(n):
        words.append(list(map(int, input().split())))

    def check(m):
        i = j = 0
        cur_height = 0
        for a, b in words:
            a *= m
            b *= m

            if a > w:
                return False
            if b != cur_height or j + a > w:
                i += cur_height
                j = 0
                cur_height = b
            if i >= h or i + b > h:
                return False
            j += a
        return True

    l, r = 0, w / max(a for a, _ in words)
    error = 1 / 10_000_000
    while r - l > error:
        m = (l + r) / 2
        if check(m):
            l = m
        else:
            r = m
    print(l)


if __name__ == '__main__':
    main()
