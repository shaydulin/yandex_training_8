from itertools import count


def main():
    s = input()
    s = s.replace(" ", "")

    ops = {
        "+": 0,
        "-": 0,
        "*": 1,
        "/": 1,
        "^": 2,
    }

    offset = iter(count(0, 6))
    ans = []

    def get_op_idx(s):
        op_idx = None
        p = 0
        for i, ch in enumerate(s):
            if ch == "(":
                p += 1
            elif ch == ")":
                p -= 1
            elif ch in ops and p == 0:
                if not op_idx:
                    op_idx = i
                elif s[op_idx] == "^":
                    if ops[ch] < ops[s[op_idx]]:
                        op_idx = i
                else:
                    if ops[ch] <= ops[s[op_idx]]:
                        op_idx = i
        return op_idx

    def parse(s: str, row):
        while len(ans) <= row:
            ans.append([])

        # print(s)
        i = 0
        while s[i] == "(":
            i += 1
        if s[0] == "(" and s.endswith(")" * i) and s.count("(") == i:
            s = s[i:-i]
        if len(s) == 1:
            cur_offset = next(offset)
            while len(ans[row]) <= cur_offset:
                ans[row].append(" ")
            ans[row][cur_offset] = s
            if row:
                while len(ans[row - 1]) <= cur_offset:
                    ans[row - 1].append(" ")
                ans[row - 1][cur_offset] = "|"
            return cur_offset, cur_offset, cur_offset

        while (op_idx := get_op_idx(s)) is None:
            s = s[1:-1]

        op = s[op_idx]
        leftmost_left, dot_left, rightmost_left = parse(s[:op_idx], row + 2)
        leftmost_right, dot_right, rightmost_right = parse(s[op_idx + 1:], row + 2)

        op_coord = (rightmost_left + leftmost_right + 1) // 2
        while len(ans[row]) <= dot_right:
            ans[row].append(" ")
        ans[row][dot_left] = "."
        ans[row][dot_right] = "."
        ans[row][dot_left + 1:dot_right] = ["-"] * (dot_right - dot_left - 1)
        ans[row][op_coord] = op
        ans[row][op_coord - 1] = "["
        ans[row][op_coord + 1] = "]"
        if row:
            while len(ans[row - 1]) <= dot_right:
                ans[row - 1].append(" ")
            ans[row - 1][op_coord] = "|"
        return leftmost_left, op_coord, rightmost_right

    parse(s, 0)
    for row in ans:
        print("".join(row))


if __name__ == '__main__':
    main()
