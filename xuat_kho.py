"""xuat_kho.py - TV3: Quản lý xuất kho (phiếu xuất, kiểm tra tồn, cập nhật số lượng)."""
from datetime import date
from du_lieu import LoiKho, chuyen_ngay, doc_so, dinh_dang_so, DINH_DANG_NGAY
from nguyen_lieu import QuanLyNguyenLieu


class ChiTietXuat:
    def __init__(self, ma_nl, so_luong):
        self.ma_nl = ma_nl
        self.so_luong = so_luong

    def to_dict(self):
        return {"ma_nl": self.ma_nl, "so_luong": self.so_luong}


class PhieuXuat:
    def __init__(self, ma_phieu, ngay, muc_dich):
        self.ma_phieu = ma_phieu
        self.ngay = ngay
        self.muc_dich = muc_dich
        self.chi_tiet = []

    def to_dict(self):
        return {"ma_phieu": self.ma_phieu, "ngay": self.ngay, "muc_dich": self.muc_dich,
                "chi_tiet": [ct.to_dict() for ct in self.chi_tiet]}


class QuanLyXuatKho:
    def __init__(self, kho):
        self.kho = kho
        self.ql_nl = QuanLyNguyenLieu(kho)

    def tao_phieu_xuat(self, ma_phieu, ngay="", muc_dich=""):
        ma_phieu = str(ma_phieu).strip().upper()
        if not ma_phieu:
            raise LoiKho("Mã phiếu không được để trống!")
        if any(p["ma_phieu"] == ma_phieu for p in self.kho.phieu_xuat):
            raise LoiKho("Mã phiếu xuất đã tồn tại!")
        ngay = str(ngay).strip() or date.today().strftime(DINH_DANG_NGAY)
        chuyen_ngay(ngay)
        return PhieuXuat(ma_phieu, ngay, str(muc_dich).strip() or "Chế biến món ăn")

    def kiem_tra_so_luong(self, ma_nl, so_luong, da_xuat=0):
        """Trả về nguyên liệu nếu đủ hàng; không đủ -> LoiKho. da_xuat: số đã xuất trong cùng phiếu."""
        nl = self.ql_nl.lay_nguyen_lieu(ma_nl)
        if so_luong <= 0:
            raise LoiKho("Số lượng phải lớn hơn 0!")
        if so_luong + da_xuat > nl.so_luong:
            raise LoiKho(f"⚠️ Không đủ nguyên liệu trong kho! (Tồn kho: {dinh_dang_so(nl.so_luong)} {nl.don_vi})")
        return nl

    def them_chi_tiet_xuat(self, phieu, ma_nl, so_luong):
        sl = doc_so(so_luong, "Số lượng")
        ma = str(ma_nl).strip().upper()
        da_xuat = sum(ct.so_luong for ct in phieu.chi_tiet if ct.ma_nl == ma)
        nl = self.kiem_tra_so_luong(ma, sl, da_xuat)
        ct = ChiTietXuat(nl.ma, sl)
        phieu.chi_tiet.append(ct)
        return ct

    def cap_nhat_ton_kho(self, phieu):
        for ct in phieu.chi_tiet:
            nl = self.ql_nl.lay_nguyen_lieu(ct.ma_nl)
            nl.so_luong = nl.so_luong - ct.so_luong        # tồn mới = tồn cũ - xuất

    def luu_phieu(self, phieu):
        self.kho.phieu_xuat.append(phieu.to_dict())

    def hien_thi_phieu_xuat(self, phieu):
        print(f"\nPhiếu xuất: {phieu.ma_phieu}   Ngày xuất: {phieu.ngay}   Mục đích: {phieu.muc_dich}")
        for ct in phieu.chi_tiet:
            nl = self.ql_nl.lay_nguyen_lieu(ct.ma_nl)
            print(f"  - {nl.ten}: {dinh_dang_so(ct.so_luong)} {nl.don_vi}")


def menu_xuat_kho(kho):
    ql = QuanLyXuatKho(kho)
    print("\n===== XUẤT KHO =====")
    try:
        phieu = ql.tao_phieu_xuat(input("Mã phiếu: "), input("Ngày xuất (Enter = hôm nay): "),
                                  input("Mục đích (Enter = Chế biến món ăn): "))
    except LoiKho as e:
        print(f"✗ {e}")
        return
    while True:
        try:
            ma = input("Mã nguyên liệu: ")
            nl = ql.ql_nl.lay_nguyen_lieu(ma)
            print(f"Tồn kho hiện tại: {dinh_dang_so(nl.so_luong)} {nl.don_vi}")
            ql.them_chi_tiet_xuat(phieu, ma, input("Số lượng xuất: "))
        except LoiKho as e:
            print(f"✗ {e}")
            print("Không thể xuất kho.")
        if input("Thêm nguyên liệu khác vào phiếu? (c/k): ").strip().lower() != "c":
            break
    if not phieu.chi_tiet:
        print("✗ Phiếu không có chi tiết hợp lệ, đã hủy phiếu.")
        return
    ql.cap_nhat_ton_kho(phieu)
    ql.luu_phieu(phieu)
    kho.luu()
    print("✓ Xuất kho thành công!")
    for ct in phieu.chi_tiet:
        nl = ql.ql_nl.lay_nguyen_lieu(ct.ma_nl)
        print(f"Tồn kho sau xuất: {nl.ten}: {dinh_dang_so(nl.so_luong)} {nl.don_vi}")
    ql.hien_thi_phieu_xuat(phieu)
