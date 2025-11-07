from collections import Counter


def main():
    s = input()
    prev = Counter()
    ans = 1
    for i in range(len(s)):
        ans += i - prev[s[i]]
        prev[s[i]] += 1
    print(ans)


if __name__ == '__main__':
    main()
