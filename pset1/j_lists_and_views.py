import re


def main():
    patterns = {
        re.compile(r"^List ([a-z]+) = new List\(([\d,]*)\)$"): create_list,
        re.compile(r"^List ([a-z]+) = ([a-z]+)\.subList\((\d+),(\d+)\)$"): create_sublist,
        re.compile(r"^([a-z]+)\.set\((\d+),(\d+)\)$"): set_value,
        re.compile(r"^([a-z]+)\.add\((\d+)\)$"): add_value,
        re.compile(r"^([a-z]+)\.get\((\d+)\)$"): get_value,
    }
    lists = {}

    with open("input.txt") as file:
        n = int(file.readline())

        for _ in range(n):
            op = file.readline().strip()
            for pattern, func in patterns.items():
                m = pattern.match(op)
                if m:
                    res = func(lists, *m.groups())
                    if res is not None:
                        print(res)
                    break


def create_list(lists, name, args_string):
    nums = args_string.split(",") if args_string else []
    lists[name] = List(nums)


def create_sublist(lists, name, base_list, from_idx, to_idx):
    base_list, offset = lists[base_list].get_base_list_and_offset()
    lists[name] = SubList(base_list, int(from_idx) + offset, int(to_idx) + offset)


def set_value(lists, lst, idx, val):
    lists[lst].set_value(int(idx), val)


def add_value(lists, lst, val):
    lists[lst].add_value(val)


def get_value(lists, lst, idx):
    return lists[lst].get_value(int(idx))


class List:
    def __init__(self, nums):
        self.nums = [0] + nums

    def set_value(self, idx, val):
        self.nums[idx] = val

    def add_value(self, val):
        self.nums.append(val)

    def get_value(self, idx):
        return self.nums[idx]

    def get_base_list_and_offset(self):
        return self, 0


class SubList:
    def __init__(self, base_list, from_idx, to_idx):
        self.base_list: List|SubList = base_list
        self.from_idx = from_idx
        self.to_idx = to_idx

    def set_value(self, idx, val):
        self.base_list.set_value(idx + self.from_idx - 1, val)

    def add_value(self, val):
        pass

    def get_value(self, idx):
        return self.base_list.get_value(idx + self.from_idx - 1)

    def get_base_list_and_offset(self):
        return self.base_list, self.from_idx - 1


if __name__ == '__main__':
    main()
