#!/usr/bin/env python3
"""
Gợi ý: có thể dùng enumerate()
https://docs.python.org/3/library/functions.html#enumerate
"""


data = ["I", "Love", "You", "Chiu", "Chiu"]


def solve(input_data):
    """Trả về 1 `list` các `list` theo định dạng sau:

        result = [[1, "I"], [2, "Love"], [3, "You"], [4, "Chiu"], [5, "Chiu"]]

    :rtype: list
    """
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    lis =[]
    for i, dt in enumerate(input_data, 1):
       lis.append([i,dt])
    print(lis)
    result = lis

    return result


def main():
    # xử lí in ra theo yêu cầu đề bài bên dưới
    result = solve(data)

    pass


if __name__ == "__main__":
    main()
