def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    dif_x = abs(x1 - x2)
    dif_y = abs(y1 - y2)

    ans = 0
    if dif_x:
        ans += 3 * (dif_x - 1)
    if dif_y:
        ans += 3 * (dif_y - 1)
    if dif_x and dif_y:
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
