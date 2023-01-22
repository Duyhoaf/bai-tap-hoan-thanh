#!/usr/bin/env python3


def solve(input_data):
    """Kiểm tra input_data có phải là palindrome không.

    Một string được gọi là `palindrome` nếu viết xuôi hay ngược đều thu được
    kết quả như nhau (không phân biệt hoa thường, bỏ qua dấu space).
    String phải dài hơn 2 chữ cái.
    Ví dụ các palindrome: 'civic', 'Able was I ere I saw Elba', 'Noon'

    :rtype: bool
    """
    result = None
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    s = input_data.lower()
    s1 = s.replace(' ', '')
    lis = list(reversed(s1))
    s2 = ''.join(lis)
    if s1 == s2:
        result = input_data + ' là palindrome! '
    else:
        result = ' khong phai là palindrome!'
    return result

def main():
    print(solve("Able was I ere I saw Elba"))

if __name__ == "__main__":
    main()
