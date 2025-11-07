def main():
    MINS = 1440

    office_1_buses = [0] * MINS
    office_2_buses = [0] * MINS

    n = int(input())
    for _ in range(n):
        departure, arrival = map(
            lambda t: int(t[:2]) * 60 + int(t[3:]),
            input().split("-"),
        )
        office_1_buses[departure] -= 1
        office_2_buses[arrival] += 1

    m = int(input())
    for _ in range(m):
        departure, arrival = map(
            lambda t: int(t[:2]) * 60 + int(t[3:]),
            input().split("-"),
        )
        office_2_buses[departure] -= 1
        office_1_buses[arrival] += 1

    ans = cur_1 = cur_2 = 0
    for i in range(MINS):
        cur_1 += office_1_buses[i]
        if cur_1 < 0:
            ans += -cur_1
            cur_1 = 0

        cur_2 += office_2_buses[i]
        if cur_2 < 0:
            ans += -cur_2
            cur_2 = 0

    print(ans)


if __name__ == '__main__':
    main()
