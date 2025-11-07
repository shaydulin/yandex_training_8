from collections import defaultdict
from heapq import nsmallest
import sys


sys.setrecursionlimit(1_000_000)

def main():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    if n == 2:
        print(1)
        return

    def traversal(root, parent):
        if len(graph[root]) == 1:
            return float("inf"), 1

        depths = []
        res = float("inf")
        for child in graph[root]:
            if child == parent:
                continue
            cur_res, depth = traversal(child, root)
            res = min(res, cur_res)
            depths.append(depth)

        if len(depths) > 1:
            res = min(res, sum(nsmallest(2, depths)))

        return res, min(depths) + 1

    ans, _ = traversal(
        next(a for a in range(1, n) if len(graph[a]) > 1),
        None,
    )
    print(ans)


if __name__ == '__main__':
    main()
