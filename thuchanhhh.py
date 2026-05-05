import math

# Định nghĩa các hàm lambda theo đúng yêu cầu đề bài (image_1f835e.jpg)
# a) Trị tuyệt đối của n
ham_a = lambda n: abs(n)

# b) Trả về giá trị n + 15
ham_b = lambda n: n + 15

# c) Tích của x và y
ham_c = lambda x, y: x * y

# d) n có là bội số của 13 hoặc 19 không?
ham_d = lambda n: n % 13 == 0 or n % 19 == 0

# e) Diện tích hình tròn (S = pi * r^2)
ham_e = lambda r: math.pi * (r ** 2)

# f) Chu vi hình chữ nhật (P = (d + r) * 2)
ham_f = lambda d, r: (d + r) * 2

# g) Kiểm tra số chính phương
ham_g = lambda n: n >= 0 and math.isqrt(n)**2 == n

# h) Kiểm tra số nguyên tố
ham_h = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

# i) Kiểm tra 3 cạnh tam giác và loại tam giác
ham_i = lambda a, b, c: (
    "Tam giác đều" if a == b == c else
    "Tam giác cân" if a == b or b == c or a == c else
    "Tam giác vuông" if (round(a**2 + b**2, 2) == round(c**2, 2) or 
                         round(a**2 + c**2, 2) == round(b**2, 2) or 
                         round(b**2 + c**2, 2) == round(a**2, 2)) else
    "Tam giác thường"
) if (a + b > c and a + c > b and b + c > a) else "Không phải 3 cạnh tam giác"

# --- CHƯƠNG TRÌNH CHÍNH CHO PHÉP NHẬP LIỆU NHIỀU LẦN ---
while True:
    print("\n--- THỰC HÀNH LAMBDA ---")
    print("Chọn chức năng để kiểm tra (a-i) hoặc 'q' để thoát:")
    chon = input("Lựa chọn của bạn: ").lower()

    if chon == 'q':
        break

    try:
        if chon == 'a':
            n = int(input("Nhập số nguyên n: "))
            print(f"Trị tuyệt đối của {n} là: {ham_a(n)}")
        elif chon == 'b':
            n = int(input("Nhập số nguyên n: "))
            print(f"Giá trị {n} + 15 là: {ham_b(n)}")
        elif chon == 'c':
            x = int(input("Nhập x: "))
            y = int(input("Nhập y: "))
            print(f"Tích {x} * {y} là: {ham_c(x, y)}")
        elif chon == 'd':
            n = int(input("Nhập số nguyên n: "))
            print(f"{n} có là bội của 13 hoặc 19? {'Có' if ham_d(n) else 'Không'}")
        elif chon == 'e':
            r = float(input("Nhập bán kính r: "))
            print(f"Diện tích hình tròn là: {ham_e(r):.2f}")
        elif chon == 'f':
            d = float(input("Nhập chiều dài d: "))
            r = float(input("Nhập chiều rộng r: "))
            print(f"Chu vi hình chữ nhật là: {ham_f(d, r)}")
        elif chon == 'g':
            n = int(input("Nhập số nguyên n: "))
            print(f"{n} có là số chính phương? {'Có' if ham_g(n) else 'Không'}")
        elif chon == 'h':
            n = int(input("Nhập số nguyên n: "))
            print(f"{n} có là số nguyên tố? {'Có' if ham_h(n) else 'Không'}")
        elif chon == 'i':
            a = float(input("Nhập cạnh a: "))
            b = float(input("Nhập cạnh b: "))
            c = float(input("Nhập cạnh c: "))
            print(f"Kết quả: {ham_i(a, b, c)}")
        else:
            print("Lựa chọn không hợp lệ!")
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng số!")

    tiep_tuc = input("\nBạn có muốn thực hiện phép tính khác không? (Y/N): ").strip().upper()
    if tiep_tuc != 'Y':
        print("Đã thoát chương trình.")
        break