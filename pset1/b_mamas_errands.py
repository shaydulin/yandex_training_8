from collections import Counter


def main():
    print(calc(input()))


def calc(data):
    a, b, c, v0, v1, v2 = map(int, data.split())
    places = ["home", "supermarket", "pickpoint"]
    dists = {
        ("home", "supermarket"): a,
        ("supermarket", "home"): a,
        ("home", "pickpoint"): b,
        ("pickpoint", "home"): b,
        ("pickpoint", "supermarket"): c,
        ("supermarket", "pickpoint"): c,
    }
    speed = {
        0: v0,
        1: v1,
        2: v1,
        3: v2,
    }

    ans = float("inf")
    cur = [(
        "home", # cur_position
        0, # cur_time
        { # picks at
            "vasya": 0,
            "home": 0,
            "supermarket": 1,
            "pickpoint": 2,
        },
        Counter(), # how many times visited
    )]
    while cur:
        nxt = []
        for state in cur:
            cur_pos, t, picks, visit_num = state
            if cur_pos == "home" and picks["home"] | picks["vasya"] == 3:
                ans = min(ans, t)
            elif visit_num[cur_pos] >= 4:
                pass
            else:
                visit_num[cur_pos] += 1

                if cur_pos == "home":
                    picks["home"] |= picks["vasya"]
                    picks["vasya"] = 0

                for place in places:
                    if place == cur_pos:
                        continue
                    nxt.append([
                        place,
                        t + dists[(cur_pos, place)] / speed[picks["vasya"]],
                        picks.copy(),
                        visit_num.copy(),
                    ])
                    if cur_pos != "home" and picks[cur_pos]:
                        picks_ = picks.copy()
                        picks_["vasya"] |= picks[cur_pos]
                        picks_[cur_pos] = 0
                        nxt.append([
                            place,
                            t + dists[(cur_pos, place)] / speed[picks_["vasya"]],
                            picks_,
                            visit_num.copy(),
                        ])
        cur = nxt
    return ans


if __name__ == '__main__':
    main()


# tests = [
#     ["1 2 2 10 10 10", 0.500000000000000],
#     ["4 1 2 5 5 5", 1.200000000000000],
#     ["2 3 4 7 6 5", 1.495238095238095],
#     ["1 6 3 7 6 5", 1.271428571428571],
#     ["2 3 4 10 9 2", 1.055555555555556],
# ]
# for test, res in tests:
#     print(calc(test), res)
