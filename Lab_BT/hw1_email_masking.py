#Bai1_email_masking
# 1.Nhập dữ liệu
ho_ten = input("Nhập họ tên: ")
raw_email = input("Nhập email: ")

# 2. Xử lý dữ liệu
parts = raw_email.split("@")
ten_email = parts[0]
mien_email = parts[1]

# 3.Mã hóa email
ten_email_ma_hoa = ten_email[0:3]

# 4. In kết quả
print("================kết quả=================".upper())
print(f"Họ Và tên: {ho_ten}")
print(f"Email: {ten_email_ma_hoa}***@{mien_email}")
print("=" * 40)
print("========cảm ơn quý khách================".upper())