def get_num_words(txt: str) -> int:
    return len(txt.split())


def get_num_char(txt: str) -> dict[str, int]:
    res = {}
    for char in txt:
        c = char.lower()
        if c not in res:
            res[c] = 0
        res[c] += 1
    return res


def sort_by_count(stats: dict[str, int]) -> list[dict[str, int]]:
    lst = []

    for k, v in stats.items():
        lst.append({"char": k, "num": v})

    def sort_on(items):
        return items["num"]

    lst.sort(key=sort_on, reverse=True)
    return lst
