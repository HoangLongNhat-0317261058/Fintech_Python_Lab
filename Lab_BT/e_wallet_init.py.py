# Bài 1: Homework
# Mở ví điện tử ban đầu
print("=== HỆ THỐNG MỞ VÍ ĐIỆN TỬ ===")

# 1. Nhập thông tin khách hàng từ bàn phím
ho_ten_raw = input("Nhập họ và tên khách hàng: ")
so_dien_thoai_input = input("Nhập số điện thoại khách hàng: ")
so_cccd_input = input("Nhập số cân cước công dân khách hàng: ")

# Ép kiểu int() để tính toán
so_tien_nap_ban_dau_input = int(input("Nhập số tiền muốn nạp (VD: 500000): "))

# 2. Trừ phí mở tài khoản
phi_mo_vi = 50000
so_du_kha_dung = so_tien_nap_ban_dau_input - phi_mo_vi

# 3. Xử lý chuẩn hóa dữ liệu
# .strip() Loại bỏ khoảng trắng thừa ở đầu/cuối chuỗi
# .upper() Viết hoa toàn bộ ho và tên
ho_ten_chuan = ho_ten_raw.strip().upper()

# 4. In biên lai khởi tạo ví bằng F-string
print("\n" + "=" * 45)
print("     MỞ VÍ ĐIỆN TỬ THÀNH CÔNG     ")
print("=" * 45)
print(f"Họ và tên: {ho_ten_chuan}")
print(f"Số điện thoại: {so_dien_thoai_input}")
print(f"Số cân cước công dân: {so_cccd_input[:8]}")
print(f"số tiền nạp: {so_tien_nap_ban_dau_input:,} VND")
print(f"phí mở ví: {phi_mo_vi:,} VND")
print(f"số dư khả dụng: {so_du_kha_dung:,} VND")
print("=" * 45)
print("Cảm ơn quý khách đã sử dụng dịch vụ")


