"""kiem_thu.py - Chạy kịch bản kiểm thử/demo tự động (giả lập người dùng gõ phím) trên dữ liệu tạm.
Chạy:  python kiem_thu.py        (không đụng tới data.json thật)"""
import builtins
import os
import sys
import tempfile
from datetime import date

from du_lieu import KhoDuLieu
from nguyen_lieu import menu_nguyen_lieu
from nhap_kho import menu_nhap_kho
from xuat_kho import menu_xuat_kho
from thong_ke import ThongKe


def chay(ham, dong_nhap, *tham_so):
    """Chạy ham với các dòng nhập giả lập; in cả câu hỏi lẫn câu trả lời như khi gõ thật."""
    it = iter(dong_nhap)

    def input_gia(prompt=""):
        tra_loi = next(it)
        print(f"{prompt}{tra_loi}")
        return tra_loi

    goc = builtins.input
    builtins.input = input_gia
    try:
        ham(*tham_so)
    finally:
        builtins.input = goc


def tieu_de(s):
    print("\n" + "#" * 8 + f" {s} " + "#" * 8)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    thu_muc = tempfile.mkdtemp()
    kho = KhoDuLieu(os.path.join(thu_muc, "kiem_thu.json"))
    kho.doc()
    hom_nay = date.today().strftime("%d/%m/%Y")

    tieu_de("TV1 - QUẢN LÝ NGUYÊN LIỆU")
    chay(menu_nguyen_lieu, [
        "1", "NL01", "Thịt gà", "Thịt", "kg", "20", "80000", "10/12/2026",
        "1", "NL01", "Thịt bò", "Thịt", "kg", "5", "250000", "",                 # trùng mã
        "1", "NL02", "", "Rau", "kg", "2", "15000", "",                          # tên trống
        "1", "NL02", "Rau cải", "Rau", "kg", "-2", "15000", "",                  # số lượng âm
        "1", "NL02", "Rau cải", "Rau", "kg", "2", "-15000", "",                  # đơn giá âm
        "1", "NL02", "Rau cải", "Rau", "kg", "2", "15000", "20/10/2026",
        "1", "NL03", "Nước mắm", "Gia vị", "chai", "1", "45000", "",
        "1", "NL04", "Thịt bò", "Thịt", "kg", "8", "250000", "28/10/2026",
        "2", "3", "thịt", "4", "NL03", "", "", "", "", "50000", "", "2",         # sửa đơn giá rồi hiển thị
        "4", "NL99", "5", "NL99", "5", "NL03", "2", "0"], kho)

    tieu_de("TV2 - NHẬP KHO")
    chay(menu_nhap_kho, [
        "PN01", hom_nay,
        "NL99", "10", "75000", "c",          # mã không tồn tại
        "NL01", "-5", "75000", "c",          # số lượng âm
        "NL01", "10", "75000", "k"], kho)

    tieu_de("TV3 - XUẤT KHO")
    chay(menu_xuat_kho, ["PX01", hom_nay, "", "NL01", "5", "k"], kho)
    chay(menu_xuat_kho, ["PX02", hom_nay, "", "NL01", "50", "k"], kho)   # không đủ hàng

    tieu_de("TV4 - THỐNG KÊ + CẢNH BÁO")
    tk = ThongKe(kho)
    tk.in_thong_ke()
    tk.in_canh_bao_ton_kho()
    tk.in_han_su_dung()

    tieu_de("KIỂM TRA LƯU / ĐỌC FILE")
    kho.luu()
    kho2 = KhoDuLieu(kho.duong_dan)
    kho2.doc()
    print(f"Đọc lại từ file: {len(kho2.nguyen_lieu)} nguyên liệu, {len(kho2.phieu_nhap)} phiếu nhập, "
          f"{len(kho2.phieu_xuat)} phiếu xuất")
    print("Tồn Thịt gà sau khi đọc lại:", kho2.nguyen_lieu[0].so_luong, "kg")


if __name__ == "__main__":
    main()
