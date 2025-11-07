from bisect import bisect_left


def main():
    n = int(input())
    intervals = []
    timestamps = {0.0}
    for _ in range(n):
        intervals.append(tuple(map(float, input().split())))
        timestamps.add(intervals[-1][1])
    intervals.sort()
    ans = [[timestamp, 0] for timestamp in sorted(timestamps)]

    i = 0
    mx_weight = 0
    for begin, end, weight in intervals:
        while ans[i][0] <= begin:
            mx_weight = max(mx_weight, ans[i][1])
            i += 1

        end_idx = bisect_left(
            ans,
            end,
            key=lambda weight_at_t: weight_at_t[0],
        )
        ans[end_idx][1] = max(ans[end_idx][1], mx_weight + weight)

    print(max(weight for _, weight in ans))


if __name__ == '__main__':
    main()
