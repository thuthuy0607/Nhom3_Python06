"""main.py - Chương trình chính: ghép các module thành menu quản lý kho nguyên liệu."""
import sys
from du_lieu import KhoDuLieu, LoiKho
from nguyen_lieu import menu_nguyen_lieu, QuanLyNguyenLieu
from nhap_kho import menu_nhap_kho
from xuat_kho import menu_xuat_kho
from thong_ke import ThongKe

RONG = 40


def in_menu():
    dong = "═" * RONG
    muc = ["1. Quản lý nguyên liệu", "2. Nhập kho", "3. Xuất kho", "4. Tìm kiếm nguyên liệu",
           "5. Thống kê kho", "6. Cảnh báo tồn kho", "7. Kiểm tra hạn sử dụng", "0. Thoát"]
    print(f"\n╔{dong}╗")
    print(f"║{'QUẢN LÝ KHO NGUYÊN LIỆU'.center(RONG)}║")
    print(f"╠{dong}╣")
    for m in muc:
        print(f"║ {m.ljust(RONG - 1)}║")
    print(f"╚{dong}╝")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    kho = KhoDuLieu()
    try:
        kho.doc()
    except LoiKho as e:
        print(f"✗ {e}")
        return
    ql = QuanLyNguyenLieu(kho)
    tk = ThongKe(kho)
    while True:
        in_menu()
        try:
            chon = input("Chọn chức năng: ").strip()
        except EOFError:
            break
        try:
            if chon == "1":
                menu_nguyen_lieu(kho)
            elif chon == "2":
                menu_nhap_kho(kho)
            elif chon == "3":
                menu_xuat_kho(kho)
            elif chon == "4":
                ql.hien_thi_danh_sach(ql.tim_nguyen_lieu(input("Nhập mã/tên cần tìm: ")))
            elif chon == "5":
                tk.in_thong_ke()
            elif chon == "6":
                tk.in_canh_bao_ton_kho()
            elif chon == "7":
                tk.in_han_su_dung()
            elif chon == "0":
                print("Tạm biệt!")
                break
            else:
                print("✗ Lựa chọn không hợp lệ!")
        except LoiKho as e:
            print(f"✗ {e}")


if __name__ == "__main__":
    main()
