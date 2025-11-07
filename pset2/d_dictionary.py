from functools import cache
from itertools import pairwise


def main():
    txt = input().strip()
    d = set()
    for _ in range(int(input())):
        d.add(input().strip())

    n = int(len(txt))
    mx_len = max(len(word) for word in d)
    ans = [0]

    @cache
    def backtrack(i):
        if i == n:
            return 1
        for j in range(i + 1, i + mx_len + 1):
            if txt[i:j] in d:
                ans.append(j)
                if backtrack(j):
                    return 1
                ans.pop()
        return 0
    
    backtrack(0)
    print(" ".join(txt[i:j] for i, j in pairwise(ans)))


if __name__ == '__main__':
    main()
