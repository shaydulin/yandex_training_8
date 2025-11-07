from collections import deque
import sys


sys.setrecursionlimit(10_000)

def main():
    n, k = map(int, input().split())
    cols = list(map(int, input().split()))

    @cache_
    def backtrack(i):
        if n - i < k:
            return 0, []

        mn_q = deque()
        sm = 0
        for j in range(i, i + k):
            sm += cols[j]
            while mn_q and mn_q[-1] > cols[j]:
                mn_q.pop()
            mn_q.append(cols[j])

        res_nxt, arr = backtrack(i + k)
        res = sm * mn_q[0] + res_nxt
        ans = [i] + arr

        for j in range(i + k, min(n, i + 2 * k - 1)):
            sm -= cols[j - k]
            if mn_q[0] == cols[j - k]:
                mn_q.popleft()

            sm += cols[j]
            while mn_q and mn_q[-1] > cols[j]:
                mn_q.pop()
            mn_q.append(cols[j])
            res_nxt, arr = backtrack(j + 1)
            if sm * mn_q[0] + res_nxt > res:
                res = sm * mn_q[0] + res_nxt
                ans = [j - k + 1] + arr

        return res, ans

    _, ans = backtrack(0)
    ans = [i + 1 for i in ans]
    print(len(ans))
    print(*ans)


def cache_(func):
    data = {}
    def wrapper(*args):
        if args not in data:
            data[args] = func(*args)
        return data[args]
    return wrapper

if __name__ == '__main__':
    main()
