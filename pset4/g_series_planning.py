def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = list(map(int, input().split()))

    idcs = sorted(range(n), key=lambda i: s[i])
    ans = [0] * n
    prev = 0
    pre_sum_a = 0
    pre_sum = 0
    for i in idcs:
        pre_sum += (s[i] - prev) * pre_sum_a
        ans[i] += pre_sum
        prev = s[i]
        pre_sum_a += a[i]

    nxt = 0
    post_sum_a = 0
    post_sum = 0
    for i in reversed(idcs):
        post_sum += (nxt - s[i]) * post_sum_a
        ans[i] += post_sum
        nxt = s[i]
        post_sum_a += a[i]

    mn_i = min(range(n), key=lambda i: (ans[i], s[i]))
    print(s[mn_i], ans[mn_i])


if __name__ == '__main__':
    main()
