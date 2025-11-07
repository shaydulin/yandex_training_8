def main():
    n, l = map(int, input().split())
    dp = [] # arrs of [cost, len_bought, len_left_before_buy]
    cur = [[float("inf"), 0, None] for _ in range(l + 1)]
    cur[l][0] = 0
    for _ in range(n):
        nxt = [[float("inf"), 0, None] for _ in range(l + 1)]
        p, r, q, f = map(int, input().split())

        for left in range(l + 1):
            for buy in range(f + 1):
                price = p if buy < r else q
                if cur[left][0] + buy * price < nxt[max(0, left - buy)][0]:
                    nxt[max(0, left - buy)] = [cur[left][0] + buy * price, buy, left]

        dp.append(nxt)
        cur = nxt

    if dp[-1][0][0] == float("inf"):
        print(-1)
        return

    print(dp[-1][0][0])
    ans = [0] * n
    left = 0
    for store in range(n - 1, -1, -1):
        _, buy, left = dp[store][left]
        ans[store] = buy
    print(*ans)


if __name__ == '__main__':
    main()
