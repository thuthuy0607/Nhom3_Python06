"""nhap_kho.py - TV2: Quản lý nhập kho (phiếu nhập, cập nhật tồn kho, tính tiền)."""
from datetime import date
from du_lieu import LoiKho, chuyen_ngay, doc_so, dinh_dang_so, dinh_dang_tien, DINH_DANG_NGAY
from nguyen_lieu import QuanLyNguyenLieu


class ChiTietNhap:
    def __init__(self, ma_nl, so_luong, don_gia):
        self.ma_nl = ma_nl
        self.so_luong = so_luong
        self.don_gia = don_gia

    @property
    def thanh_tien(self):
        return self.so_luong * self.don_gia

    def to_dict(self):
        return {"ma_nl": self.ma_nl, "so_luong": self.so_luong, "don_gia": self.don_gia}


class PhieuNhap:
    def __init__(self, ma_phieu, ngay):
        self.ma_phieu = ma_phieu
        self.ngay = ngay
        self.chi_tiet = []

    @property
    def tong_tien(self):
        return sum(ct.thanh_tien for ct in self.chi_tiet)

    def to_dict(self):
        return {"ma_phieu": self.ma_phieu, "ngay": self.ngay,
                "chi_tiet": [ct.to_dict() for ct in self.chi_tiet], "tong_tien": self.tong_tien}


class QuanLyNhapKho:
    def __init__(self, kho):
        self.kho = kho
        self.ql_nl = QuanLyNguyenLieu(kho)

    def tao_phieu_nhap(self, ma_phieu, ngay=""):
        ma_phieu = str(ma_phieu).strip().upper()
        if not ma_phieu:
            raise LoiKho("Mã phiếu không được để trống!")
        if any(p["ma_phieu"] == ma_phieu for p in self.kho.phieu_nhap):
            raise LoiKho("Mã phiếu nhập đã tồn tại!")
        ngay = str(ngay).strip() or date.today().strftime(DINH_DANG_NGAY)
        chuyen_ngay(ngay)
        return PhieuNhap(ma_phieu, ngay)

    def them_chi_tiet_nhap(self, phieu, ma_nl, so_luong, don_gia):
        nl = self.ql_nl.lay_nguyen_lieu(ma_nl)            # mã phải tồn tại
        sl = doc_so(so_luong, "Số lượng")
        if sl <= 0:
            raise LoiKho("Số lượng phải lớn hơn 0!")
        gia = doc_so(don_gia, "Đơn giá")
        if gia <= 0:
            raise LoiKho("Đơn giá phải lớn hơn 0!")
        ct = ChiTietNhap(nl.ma, sl, gia)
        phieu.chi_tiet.append(ct)
        return ct

    def cap_nhat_ton_kho(self, phieu):
        for ct in phieu.chi_tiet:
            nl = self.ql_nl.lay_nguyen_lieu(ct.ma_nl)
            nl.so_luong = nl.so_luong + ct.so_luong        # tồn mới = tồn cũ + nhập

    def tinh_tien_nhap(self, phieu):
        return phieu.tong_tien

    def luu_phieu(self, phieu):
        self.kho.phieu_nhap.append(phieu.to_dict())

    def hien_thi_phieu_nhap(self, phieu):
        print(f"\nPhiếu nhập: {phieu.ma_phieu}   Ngày nhập: {phieu.ngay}")
        for ct in phieu.chi_tiet:
            nl = self.ql_nl.lay_nguyen_lieu(ct.ma_nl)
            print(f"  - {nl.ten}: {dinh_dang_so(ct.so_luong)} {nl.don_vi} x {dinh_dang_tien(ct.don_gia)}"
                  f" = {dinh_dang_tien(ct.thanh_tien)} VNĐ")
        print(f"Tổng tiền: {dinh_dang_tien(phieu.tong_tien)} VNĐ")


def menu_nhap_kho(kho):
    ql = QuanLyNhapKho(kho)
    print("\n===== NHẬP KHO =====")
    try:
        phieu = ql.tao_phieu_nhap(input("Mã phiếu: "), input("Ngày nhập (Enter = hôm nay): "))
    except LoiKho as e:
        print(f"✗ {e}")
        return
    while True:
        try:
            ma = input("Mã nguyên liệu: ")
            sl = input("Số lượng nhập: ")
            gia = input("Đơn giá: ")
            ct = ql.them_chi_tiet_nhap(phieu, ma, sl, gia)
            print(f"Thành tiền: {dinh_dang_tien(ct.thanh_tien)} VNĐ")
        except LoiKho as e:
            print(f"✗ {e}")
        if input("Thêm nguyên liệu khác vào phiếu? (c/k): ").strip().lower() != "c":
            break
    if not phieu.chi_tiet:
        print("✗ Phiếu không có chi tiết hợp lệ, đã hủy phiếu.")
        return
    ql.cap_nhat_ton_kho(phieu)
    ql.luu_phieu(phieu)
    kho.luu()
    print("✓ Nhập kho thành công!")
    for ct in phieu.chi_tiet:
        nl = ql.ql_nl.lay_nguyen_lieu(ct.ma_nl)
        print(f"Tồn kho hiện tại: {nl.ten}: {dinh_dang_so(nl.so_luong)} {nl.don_vi}")
    ql.hien_thi_phieu_nhap(phieu)
