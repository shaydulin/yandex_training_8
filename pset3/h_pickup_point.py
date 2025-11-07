import sys


sys.setrecursionlimit(1_000_000)

def main():
    n = int(input())
    residents = [0] + list(map(int, input().split()))
    total = residents.copy()
    mx = residents.copy()

    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    def bottom_up(root, parent):
        res = residents[root]
        for node in tree[root]:
            if node == parent:
                continue
            res_node = bottom_up(node, root)
            res += res_node
            mx[root] = max(mx[root], res_node)
        total[root] = res
        return res

    def top_down(root, parent, from_top):
        mx[root] = max(mx[root], from_top)
        total[root] += from_top
        for node in tree[root]:
            if node == parent:
                continue
            top_down(node, root, total[root] - total[node])

    bottom_up(1, None)
    top_down(1, None, 0)

    print(min(range(1, n + 1), key=lambda i: mx[i]))


if __name__ == '__main__':
    main()
