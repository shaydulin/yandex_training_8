from bisect import bisect_left
from itertools import accumulate


def main():
    n = int(input())
    coords_a = list(map(int, input().split()))
    m = int(input())
    coords_b = list(map(int, input().split()))

    print(calc(n, coords_a, m, coords_b))


def calc(n, coords_a, m, coords_b):
    ans = 0
    idcs_b = sorted(range(m), key=lambda i: coords_b[i])

    def f1(prev, j):
        return prev + coords_b[j]

    def f2(prev, j):
        return prev + j * coords_b[j]

    idcs_b_prefix_sum = [*accumulate(idcs_b)]
    vals_b_prefix_sum = [*accumulate(idcs_b, func=f1, initial=0)][1:]
    vals_b_mul_idcs_b_prefix_sum = [*accumulate(idcs_b, func=f2, initial=0)][1:]
    for i in range(n):
        idx = bisect_left(
            idcs_b,
            coords_a[i],
            key=lambda j: coords_b[j],
        )
        if idx > 0:
            ans += (
                (i * idx - idcs_b_prefix_sum[idx - 1]) * coords_a[i]
                -i * vals_b_prefix_sum[idx - 1]
                +vals_b_mul_idcs_b_prefix_sum[idx - 1]
            )
        if idx < m:
            idcs_sm = i * (m - idx) - (idcs_b_prefix_sum[-1] - (idcs_b_prefix_sum[idx - 1] if idx else 0))
            vals_sm = vals_b_prefix_sum[-1] - (vals_b_prefix_sum[idx - 1] if idx else 0)
            vals_mul_idcs_sm = vals_b_mul_idcs_b_prefix_sum[-1] - (vals_b_mul_idcs_b_prefix_sum[idx - 1] if idx else 0)
            ans += (
                -(idcs_sm) * coords_a[i]
                +i * (vals_sm)
                -(vals_mul_idcs_sm)
            )

    return ans


if __name__ == '__main__':
    main()
