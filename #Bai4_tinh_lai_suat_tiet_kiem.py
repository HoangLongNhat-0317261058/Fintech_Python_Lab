#Bai4_tinh_lai_suat_tiet_kiem
# 1. Nhập dữ liệu
so_tien_goc = float(input("Nhập số tiền gốc (VND): "))
lai_suat_nam = float(input("nhập lãi suất (%): "))
thoi_gian = int(input("Nhập thời gian: "))

# 2. Tính tổng tiền lãi
tong_tien = so_tien_goc * (1 + lai_suat_nam * thoi_gian)

# 3. Tạo bản mẫu
hoa_don = f"""
---------------------------
=====HÓA ĐƠN TIẾT KIỆM=====
Số tiền gốc: {so_tien_goc:,.0f} VND
Lãi suất: {lai_suat_nam} %
Thời gian: {thoi_gian} năm
Tổng tiền lãi: {tong_tien:,.0f} VND
---------------------------
=====CẢM ƠN QUÝ KHÁCH=====
---------------------------
"""
# 4. In hóa đơn
print(hoa_don)
