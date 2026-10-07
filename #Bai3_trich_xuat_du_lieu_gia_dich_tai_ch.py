#Bai3_trich_xuat_du_lieu_gia_dich_tai_chinh
# 1. thông tin 
ma_giao_dich = "GD001-5000000-VND"

# 2.Trích xuất thông tin
so_tien = ma_giao_dich[6:13]

# 3. Ép kiểu dữ liệu
so_tien = int(so_tien)

# 4. Rẽ nhánh
if so_tien >= 5000000:
    print("Cần xác thực mã OTP")
else:
    print("Giao dịch thành công")