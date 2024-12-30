import random
import json


def rand() -> int:
    return random.randint(1, 6)


my_list: list[int] = []


def get_list(lst: list[int]) -> list[int]:
    if len(lst) >= 100:
        return lst
    else:
        lst.append(rand())
        return get_list(lst)


def count_list(lst: list[int]) -> dict[str, int]:
    count_dict: dict[str, int] = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
    }
    for value in lst:
        count_dict[str(value)] += 1
        pass

    return count_dict


dict_list: list[dict[str, int]] = []


def main():
    for _ in range(100):
        my_list: list[int] = []
        ans_dict = count_list(get_list(my_list))
        dict_list.append(ans_dict)

    formatted_output_json = json.dumps(dict_list, indent=2)
    print(formatted_output_json)


if __name__ == "__main__":
    main()
