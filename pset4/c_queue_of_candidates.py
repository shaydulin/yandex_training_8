from itertools import accumulate


def main():
    n, x = map(int, input().split())
    ans = [*accumulate(map(lambda p: int(p) >= x, input().split()), initial=0)]

    cur = 0
    for _ in range(int(input())):
        q = input().strip()
        if q.startswith("1"):
            ans.append(ans[-1] + (int(q[2:]) >= x))
        elif q.startswith("2"):
            cur += 1
        else:
            print(ans[int(q[2:]) + cur] - ans[cur])


if __name__ == '__main__':
    main()
