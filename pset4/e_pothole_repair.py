from itertools import accumulate


def main():
    n, m, k = map(int, input().split())
    potholes = list(map(int, input().split()))
    freq = [0] * (n + 1)
    for _ in range(m):
        l, r = map(int, input().split())
        freq[l - 1] += 1
        freq[r] -= 1
    freq = [*accumulate(freq)]
    idcs = sorted(range(n), key=lambda i: -freq[i])
    i = 0
    for i in idcs:
        sub = min(k, potholes[i])
        k -= sub
        potholes[i] -= sub

    print(sum(f * ph for f, ph in zip(freq, potholes)))


if __name__ == '__main__':
    main()
