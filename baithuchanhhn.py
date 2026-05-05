import math

# Hàm kiểm tra số nguyên tố (Yêu cầu a)
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

danh_sach = []

# --- Vòng lặp nhập dữ liệu ---
while True:
    try:
        so = int(input("Nhập một số nguyên: "))
        danh_sach.append(so)
    except ValueError:
        print("Vui lòng chỉ nhập số nguyên!")
        continue

    # Hỏi người dùng có muốn nhập tiếp hay không
    lua_chon = input("Bạn có muốn nhập nữa hay không? (Yes/No): ").strip().lower()
    if lua_chon in ['no', 'n']:
        break

# --- Thực hiện các yêu cầu sau khi dừng nhập ---
if not danh_sach:
    print("Danh sách trống, không có gì để thực hiện.")
else:
    print("\n--- KẾT QUẢ ---")

    # a) In ra các số nguyên tố có trong list
    so_nguyen_to = [x for x in danh_sach if la_so_nguyen_to(x)]
    print(f"a) Các số nguyên tố trong list: {so_nguyen_to}")

    # b) Tính trung bình cộng các số âm và số dương
    so_am = [x for x in danh_sach if x < 0]
    so_duong = [x for x in danh_sach if x > 0]

    tbc_am = sum(so_am) / len(so_am) if so_am else "Không có số âm"
    tbc_duong = sum(so_duong) / len(so_duong) if so_duong else "Không có số dương"
    
    print(f"b) Trung bình cộng số âm: {tbc_am}")
    print(f"   Trung bình cộng số dương: {tbc_duong}")

    # c) Số lớn nhất, số nhỏ nhất
    print(f"c) Số lớn nhất: {max(danh_sach)}")
    print(f"   Số nhỏ nhất: {min(danh_sach)}")

    # d) Kiểm tra list đã được sắp xếp tăng dần hay chưa
    # Cách kiểm tra: So sánh list hiện tại với list đã qua hàm sorted()
    da_sap_xep = (danh_sach == sorted(danh_sach))
    if da_sap_xep:
        print("d) Các số trong list ĐÃ được sắp xếp tăng dần.")
    else:
        print("d) Các số trong list CHƯA được sắp xếp tăng dần.")