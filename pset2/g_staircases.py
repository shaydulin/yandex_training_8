from functools import cache


def main():
    n = int(input())

    @cache
    def backtrack(n, prev):
        if n <= 1:
            return 1
        for i in range(1, n + 1):
            if i * (i + 1) // 2 >= n:
                mn = i
                break
        res = 0
        for i in range(mn, min(prev, n + 1)):
            res += backtrack(n - i, i)

        return res
    
    ans = backtrack(n, float("inf"))
    print(ans)


if __name__ == '__main__':
    main()
