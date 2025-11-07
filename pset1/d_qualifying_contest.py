from collections import Counter


def main():
    n, k = map(int, input().split())
    topics = Counter(map(int, input().split()))
    ans = list(topics)
    while len(ans) < k:
        topic, cnt = topics.popitem()
        if cnt > 1:
            ans.extend([topic] * (cnt - 1))
    print(*ans[:k])


if __name__ == '__main__':
    main()
