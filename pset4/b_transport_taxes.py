from bisect import bisect_left


def main():
    n = int(input())
    b = [0] * n
    t = [0] * n
    for i in range(n):
        bi, ti = map(int, input().split())
        b[i] = bi
        t[i] = ti

    m = int(input())
    for i in range(m):
        q = int(input())
        print(q * t[bisect_left(b, q) - 1])


if __name__ == '__main__':
    main()
