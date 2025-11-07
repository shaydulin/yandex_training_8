def main():
    n = int(input())
    nums = list(map(int, input().split()))
    mx = max((i for i in range(1, n, 2)), key=lambda i: nums[i])
    mn = min((i for i in range(0, n, 2)), key=lambda i: nums[i])
    if nums[mx] > nums[mn]:
        nums[mx], nums[mn] = nums[mn], nums[mx]
    print(sum(nums[::2]) - sum(nums[1::2]))


if __name__ == '__main__':
    main()
