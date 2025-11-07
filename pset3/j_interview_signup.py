def main():
    n = int(input())
    want = list(map(int, input().split()))
    poss = list(map(int, input().split()))

    def check(k):
        j = 0
        want_j = want[j]
        for i in range(n):
            if i - j > k:
                return False
            
            poss_i = poss[i]

            while poss_i and j < i + k + 1 and j < n:
                to_sub = min(poss_i, want_j)
                poss_i -= to_sub
                want_j -= to_sub
                if not want_j:
                    j += 1
                    if j < n:
                        want_j = want[j]
                    else:
                        return True

        return j == n

    l, r = 0, n
    while l < r:
        m = (l + r) // 2
        if check(m):
            r = m
        else:
            l = m + 1

    print(l if l < n else -1)


if __name__ == '__main__':
    main()
