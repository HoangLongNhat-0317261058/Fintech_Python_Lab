# Nhập thông tin người dùng
ten_san_pham = input(" Nhập tên sản phẩm: ")
so_luong_san_pham = int(input(" Nhập số lượng sản phẩm: "))
don_gia = float(input(" Nhập đơn giá (VD:500000): "))

# Tính các giá trị
tong_tien_hang = so_luong_san_pham * don_gia
thue_vat = 0.08 * tong_tien_hang
tong_thanh_toan = tong_tien_hang + thue_vat

# In hóa đơn bán lẻ dạng chuỗi (string)
print("\n" + "=" * 30)
print("        HÓA ĐƠN BÁN LẺ        ")
print("=" * 30)
print(f"Tên sản phảm: {ten_san_pham}")
print(f"Số lượng: {so_luong_san_pham:}")
print(f"Đơn giá: {don_gia:,.0f}Đ")
print(f"Tổng tiền hàng: {tong_tien_hang:,.0f}Đ")
print(f"Thuế VAT (8%): {thue_vat:,.0f}Đ")
print(f"Tổng thanh toán: {tong_thanh_toan:,.0f}Đ")
print("=" * 30)
print("   CẢM ƠN QUÝ KHÁCH ĐÃ MUA HÀNG   ") 
