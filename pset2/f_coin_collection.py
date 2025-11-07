def main():
    n = int(input())
    road = []
    for _ in range(n):
        road.append(input().strip())

    cur_coins = [0, 0, 0]
    cur_pos = [1, 1, 1]
    for row in road:
        nxt_pos = [0, 0, 0]
        nxt_coins = [0, 0, 0]

        if row[0] != "W":
            if cur_pos[0]:
                nxt_pos[0] = 1
                nxt_coins[0] = cur_coins[0]
            if cur_pos[1]:
                nxt_pos[0] = 1
                nxt_coins[0] = max(nxt_coins[0], cur_coins[1])

        if row[1] != "W":
            if cur_pos[0]:
                nxt_pos[1] = 1
                nxt_coins[1] = cur_coins[0]
            if cur_pos[1]:
                nxt_pos[1] = 1
                nxt_coins[1] = max(nxt_coins[1], cur_coins[1])
            if cur_pos[2]:
                nxt_pos[1] = 1
                nxt_coins[1] = max(nxt_coins[1], cur_coins[2])

        if row[2] != "W":
            if cur_pos[1]:
                nxt_pos[2] = 1
                nxt_coins[2] = cur_coins[1]
            if cur_pos[2]:
                nxt_pos[2] = 1
                nxt_coins[2] = max(nxt_coins[2], cur_coins[2])

        if not any(nxt_pos):
            break
        cur_pos = nxt_pos
        cur_coins = nxt_coins
        cur_coins[0] += int(row[0] == "C")
        cur_coins[1] += int(row[1] == "C")
        cur_coins[2] += int(row[2] == "C")

    print(max(cur_coins))


if __name__ == '__main__':
    main()
