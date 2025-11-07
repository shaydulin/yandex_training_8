def main():
    n = int(input())
    steps = [0] * (n + 3)
    steps[0] = 1
    for i in range(n):
        steps[i + 1] += steps[i]
        steps[i + 2] += steps[i]
        steps[i + 3] += steps[i]
    print(steps[-3])


if __name__ == '__main__':
    main()
