from typing import List


def max_value(values: List[int]) -> int:
    max_val = values[0]
    for value in values:
        if value > max_val:
            max_val = value

    return max_val


def min_value(values: List[int]) -> int:
    min_val = values[0]
    for value in values:
        if value < min_val:
            min_val = value

    return min_val


# if you are running this file as a main file, run the code!
if __name__ == '__main__':
    print("Hello")