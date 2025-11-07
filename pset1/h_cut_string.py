from collections import defaultdict


def main():
    n, m = map(int, input().split())
    s = input().strip()
    subs = defaultdict(list)
    for i in range(1, m + 1):
        subs[input().strip()].append(i)
    k = n // m
    print(*(subs[s[i:i + k]].pop() for i in range(0, n, k)))


if __name__ == '__main__':
    main()
