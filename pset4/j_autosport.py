def main():
    N, L, W = map(int, input().split())
    MODELS = []
    for _ in range(N):
        MODELS.append(tuple(map(int, input().split())))

    events = []
    crush_time = [float("inf")] * N
    for i in range(N):
        x1, y1, vx1, vy1 = MODELS[i]

        for j in range(i + 1, N):
            x2, y2, vx2, vy2 = MODELS[j]

            if (x1 - x2) * (vy2 - vy1) != (y1 - y2) * (vx2 - vx1):
                continue

            n = d = 0
            if vx1 != vx2:
                n, d = x1 - x2, vx2 - vx1
            if n * d <= 0 and vy1 != vy2:
                n, d = y1 - y2, vy2 - vy1

            if n * d > 0:
                t = n / d
                if crush_time[i] >= t and crush_time[j] >= t:
                    crush_time[i] = crush_time[j] = t
                    events.append((t, 0, (i, j)))

        if vy1 > 0:
            t = (W - y1) / vy1
            if crush_time[i] >= t:
                crush_time[i] = t
                events.append((t, 0, (i,)))
        elif vy1 < 0:
            t = y1 / -vy1
            if crush_time[i] >= t:
                crush_time[i] = t
                events.append((t, 0, (i,)))

        if vx1 > 0:
            t = (L - x1) / vx1
            if crush_time[i] >= t:
                events.append((t, 1, (i,)))

    events.sort()

    winners = [] # [t, idx]
    for t, finish, models in events:
        if winners and t > winners[-1][0]:
            break

        if finish:
            if crush_time[models[0]] > t:
                winners.append((t, models[0]))
        else:
            if len(models) == 1:
                crush_time[models[0]] = t
            else:
                i, j = models
                if crush_time[i] >= t and crush_time[j] >= t:
                    crush_time[i] = crush_time[j] = t

    print(len(winners))
    print(*(i + 1 for _, i in winners))


if __name__ == '__main__':
    main()
