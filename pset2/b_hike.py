def main():
    river = input()
    cost = [0, 1] # left, right cost
    for inflow in river:
        cost = [
            min(
                cost[0] + int(inflow in "LB"),
                cost[1] + 1 + int(inflow in "RB"),
                cost[1] + 1 + int(inflow in "LB"),
            ),
            min(
                cost[1] + int(inflow in "RB"),
                cost[0] + 1 + int(inflow in "RB"),
                cost[0] + 1 + int(inflow in "LB"),
            ),
        ]
    print(cost[1])


if __name__ == '__main__':
    main()
