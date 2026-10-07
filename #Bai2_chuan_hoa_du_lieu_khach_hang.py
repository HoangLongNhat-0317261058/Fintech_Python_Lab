#Bai2_chuan_hoa_du_lieu_khach_hang
# 1. Nhập dữ liệu khách hàng
ten_khach_hang = input("Nhập tên khách hàng: ")

# 2. Chuẩn hóa dữ liệu
ten_chuan_hoa = ten_khach_hang.strip().title()

# 3. Hiện thị kết quả
print("====hệ thống chuẩn hóa====".upper())
print(f"Tên khách hàng chuẩn hóa: {ten_chuan_hoa}")
print("====cảm ơn quý khách đã sử dụng====".upper())
