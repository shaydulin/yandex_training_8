def main():
    n, k = map(int, input().split())
    while k and n % 10 != 2 and n % 10:
        n += n % 10
        k -= 1
    if n % 10 == 2:
        n += 20 * (k // 4)
    k %= 4
    while k:
        n += n % 10
        k -= 1
    print(n)


if __name__ == '__main__':
    main()
