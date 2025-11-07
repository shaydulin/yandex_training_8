import sys


sys.setrecursionlimit(1_000_000)


def main():
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    for child, parent in enumerate(map(int, input().split()), 1):
        if parent:
            tree[parent].append(child)
        else:
            root = child

    m = int(input())
    queries = [[] for _ in range(n + 1)]
    for i in range(m):
        parent, child = map(int, input().split())
        queries[parent].append((child, i))

    ans = [0] * m

    def traversal(root):
        children = 0
        for child in tree[root]:
            children |= traversal(child)

        for node, i in queries[root]:
            ans[i] = 1 if 1 << node & children else 0

        children |= 1 << root
        return children
    
    traversal(root)
    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
