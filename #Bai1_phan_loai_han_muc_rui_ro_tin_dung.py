#Bai1_phan_loai_han_muc_rui_ro_tin_dung
print("===hệ thống phân loại tín dụng===".upper())

# 1.Nhập điểm
diem = int(input("Nhập điểm tín dụng khách hàng (0-850): "))

# 2.phân loại
if diem < 0 or diem > 850:
    print("Điểm không hợp lệ. Vui lòng nhập lại.")
elif diem >= 750 and diem <= 850:
    muc_do_rui_ro = "rủi ro thấp"
    duyet = "duyệt tự động"
elif diem >= 600 and diem <= 749:
    muc_do_rui_ro = "Rủi ro trung bình"
    duyet = "Cần thẩm định"
else:
    muc_do_rui_ro = "Rủi ro cao"
    duyet = "Từ chối cấp tín dụng"

# 3.In kết quả
if 0 <= diem <=850:
    print("\n----kết quả phân loại tín dụng----".upper())
    print(f"Điểm tín dụng: {diem}")
    print(f"Mức độ rủi ro: {muc_do_rui_ro}")
    print(f"Quyết định: {duyet}")
print("===cảm ơn quý khách đã sử dụng hệ thống===".upper())