#!/usr/bin/env python3
data = 1000

def solve(input_data):
    """Đầu vào: một số nguyên dương

    Đầu ra: số nguyên tạo bởi phần từ số 1 cuối cùng trở về bên
    phải - của dạng binary của số đầu vào.

    Ví dụ::

      input_data = 5 # (0b101)
      output = 1

      input_data = 24 (11000)
      output = 1000

      input_data = 9 (1001)
      output = 1

    Hàm có sẵn: bin(10) == '0b1010'
    Hàm có sẵn tạo ra integer từ string: 69 == int('69')
    CHÚ Ý: đây là bài khó nhất chương 3, nên làm bài khác trước
    CHÚ Ý 2: code khi chạy chỉ chạy với 1 ví dụ nhưng khi
    "test" sẽ chạy với nhiều đầu vào khác nhau. Học viên
    đảm bảo xử lý dựa trên input_data, không phải data
    và làm đúng với mọi trường hợp.
    """

    result = None
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    s = bin(input_data)
    st = str(s)
    lis = list(reversed(st))
    st2 =''.join(lis)
    vt = -1 - st2.find('1')
    result = st[vt:]
    return result

def main():

    print(solve(data))


if __name__ == "__main__":
    main()
