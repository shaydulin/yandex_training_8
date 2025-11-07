from collections import defaultdict


def main():
    n, m, x = map(int, input().split())
    occupation = defaultdict(int)

    for _ in range(n):
        a, b, v = map(int, input().split())
        if a < b:
            if b <= x:
                occupation[(x - b) / v] += 1
                occupation[(x - a) / v] -= 1
            elif a < x:
                occupation[0] += 1
                occupation[(x - a) / v] -= 1
        elif a > b:
            if b >= x:
                occupation[(b - x) / v] += 1
                occupation[(a - x) / v] -= 1
            elif a > x:
                occupation[0] += 1
                occupation[(a - x) / v] -= 1


    car_arrival_t = list(map(int, input().split()))

    ans = [0] * m
    cars_order = sorted(range(m), key=lambda i: car_arrival_t[i])
    i = 0
    cur_occupation = 0
    for t, trains in sorted(occupation.items()):
        if trains == 0:
            continue

        if cur_occupation == 0:
            while i < m and car_arrival_t[cars_order[i]] < t:
                ans[cars_order[i]] = car_arrival_t[cars_order[i]]
                i += 1

        cur_occupation += trains

        if cur_occupation == 0:
            while i < m and car_arrival_t[cars_order[i]] <= t:
                ans[cars_order[i]] = t
                i += 1

    while i < m:
        ans[cars_order[i]] = max(t, car_arrival_t[cars_order[i]])
        i += 1

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
