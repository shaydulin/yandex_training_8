from bisect import bisect_left


def main():
    n, p = map(int, input().split())
    nums = list(map(int, input().split()))
    idcs = sorted(range(n), key=lambda i: nums[i])

    dif = float("inf")
    ans = [None, None]
    for i in idcs:
        j_idx = bisect_left(
            idcs,
            nums[i] / p,
            key=lambda idx: nums[idx],
        )
        for j_idx in range(j_idx - 2, j_idx + 2):
            if j_idx < 0 or j_idx >= n or idcs[j_idx] == i:
                continue
            j = idcs[j_idx]
            if abs(nums[i] / nums[j] - p) < dif:
                dif = abs(nums[i] / nums[j] - p)
                ans = [i + 1, j + 1]

    print(*ans)


if __name__ == '__main__':
    main()
