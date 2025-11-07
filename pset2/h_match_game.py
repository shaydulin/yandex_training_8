def main():
    n = int(input())
    primes = [1] * (n + 1)
    primes[0] = primes[1] = 0
    for i in range(2, n + 1):
        if not primes[i]:
            continue
        for j in range(i * i, n + 1, i):
            primes[j] = 0

    first_win = [0] * (n + 1)
    for i in range(min(4, n + 1)):
        first_win[i] = 1

    for i in range(4, n + 1):
        cur = 1
        for j in range(1, 4):
            if not primes[i - j]:
                cur &= first_win[i - j]
        first_win[i] = 1 ^ cur

    print(1 if first_win[n] else 2)


if __name__ == '__main__':
    main()
