#Bai2_promo_code
# 1. nhập dữ liệu
ho_ten = input("Nhập họ và tên: ")
nam_sinh = int(input("Nhập năm sinh: "))

# 2. Xử lý dữ liệu
parts = ho_ten.split(" ")
ho = parts[0]
ten_dem = parts[1]
ten = parts[2]

# cắt và viết hoa
ten_cat = ten[0:3].upper()

# 3.In kết quả
print("============tặng mã khuyến mãi===============".upper())
print(f"Họ và tên: {ho_ten}")
print(f"Năm sinh: {nam_sinh}")
print(f"Mã khuyến mãi: {ten_cat}-{nam_sinh}-VIP")
print("=" * 40)
print("============cảm ơn quý khách================".upper())