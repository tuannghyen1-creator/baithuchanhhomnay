from collections import Counter

# Cho phép người dùng nhập 2 chuỗi S1 và S2
s1 = input("Nhập chuỗi S1: ")
s2 = input("Nhập chuỗi S2: ")

# --- CÂU A ---
# Gợi ý: sử dụng class Counter trong module collections và phép toán &
counter1 = Counter(s1)
counter2 = Counter(s2)

# Phép toán & trên 2 Counter sẽ trả về các ký tự xuất hiện ở cả hai (với số lượng tối thiểu)
giao_nhau = counter1 & counter2

print("\na) Những ký tự xuất hiện trong cả 2 chuỗi:")
# In ra các key (ký tự) trong kết quả phép &
print(list(giao_nhau.keys()))


# --- CÂU B & C ---
# Gợi ý: đưa mỗi chuỗi vào 1 dict và thực hiện dò tìm chéo
dict1 = Counter(s1) # Đã là dict thuộc class Counter
dict2 = Counter(s2)

# Tìm ký tự có trong S1 nhưng không có trong S2
s1_khong_trong_s2 = [char for char in dict1 if char not in dict2]

# Tìm ký tự có trong S2 nhưng không có trong S1
s2_khong_trong_s1 = [char for char in dict2 if char not in dict1]

# Kết quả câu b: Đếm số lượng
print("\nb) Số lượng ký tự:")
print(f"- Có trong S1 nhưng không có trong S2: {len(s1_khong_trong_s2)}")
print(f"- Có trong S2 nhưng không có trong S1: {len(s2_khong_trong_s1)}")

# Kết quả câu c: In ra các ký tự đó
print("\nc) Các ký tự cụ thể:")
print(f"- Có trong S1 nhưng không có trong S2: {s1_khong_trong_s2}")
print(f"- Có trong S2 nhưng không có trong S1: {s2_khong_trong_s1}")