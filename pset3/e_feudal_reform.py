import sys


sys.setrecursionlimit(1_000_000)

def main():
    n = int(input())
    tree = [[] for _ in range(n)]
    for i in range(1, n):
        tree[int(input())].append(i)
    vals = list(map(int, input().split()))

    def traversal(root):
        if not tree[root]:
            return -vals[root], abs(vals[root])

        correction = 0
        total = 0

        for child in tree[root]:
            child_correction, child_total = traversal(child)
            correction += child_correction
            total += child_total

        dif = vals[root] + correction

        return correction - dif, total + abs(dif)

    print(traversal(0)[1])


if __name__ == '__main__':
    main()
