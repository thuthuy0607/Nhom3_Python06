"""nguyen_lieu.py - TV1: Quản lý nguyên liệu (thiết kế dữ liệu + các hàm xử lý)."""
from datetime import date
from du_lieu import LoiKho, chuyen_ngay, doc_so, dinh_dang_so, dinh_dang_tien, DINH_DANG_NGAY


class NguyenLieu:
    """Lớp cơ sở: nguyên liệu thường (khô, đóng chai, gia vị...)."""
    NHOM = "Thường"
    NGUONG_SAP_HET = 5            # tồn <= ngưỡng này thì cảnh báo sắp hết
    NGAY_CANH_BAO_HET_HAN = 30    # còn <= số ngày này thì cảnh báo sắp hết hạn

    def __init__(self, ma, ten, loai, don_vi, so_luong, don_gia, han_su_dung=""):
        self.ma = ma
        self.ten = ten
        self.loai = loai
        self.don_vi = don_vi
        self.so_luong = so_luong
        self.don_gia = don_gia
        self.han_su_dung = han_su_dung

    # ----- thuộc tính có kiểm tra dữ liệu (encapsulation) -----
    @property
    def ma(self):
        return self._ma

    @ma.setter
    def ma(self, v):
        v = str(v).strip().upper()
        if not v:
            raise LoiKho("Mã nguyên liệu không được để trống!")
        self._ma = v

    @property
    def ten(self):
        return self._ten

    @ten.setter
    def ten(self, v):
        v = str(v).strip()
        if not v:
            raise LoiKho("Tên nguyên liệu không được để trống!")
        self._ten = v

    @property
    def so_luong(self):
        return self._so_luong

    @so_luong.setter
    def so_luong(self, v):
        v = v if isinstance(v, (int, float)) else doc_so(v, "Số lượng")
        if v < 0:
            raise LoiKho("Số lượng không được âm!")
        self._so_luong = int(v) if float(v).is_integer() else v

    @property
    def don_gia(self):
        return self._don_gia

    @don_gia.setter
    def don_gia(self, v):
        v = v if isinstance(v, (int, float)) else doc_so(v, "Đơn giá")
        if v < 0:
            raise LoiKho("Đơn giá không được âm!")
        self._don_gia = int(v) if float(v).is_integer() else v

    @property
    def han_su_dung(self):
        return self._han_su_dung

    @han_su_dung.setter
    def han_su_dung(self, v):
        v = str(v).strip()
        if v:
            chuyen_ngay(v)  # kiểm tra định dạng
        self._han_su_dung = v

    # ----- nghiệp vụ -----
    def gia_tri_ton(self):
        return self.so_luong * self.don_gia

    def sap_het(self):
        return self.so_luong <= self.NGUONG_SAP_HET

    def so_ngay_con_han(self, hom_nay=None):
        if not self.han_su_dung:
            return None
        hom_nay = hom_nay or date.today()
        return (chuyen_ngay(self.han_su_dung) - hom_nay).days

    def trang_thai_han(self, hom_nay=None):
        """Trả về 'khong_han' | 'het_han' | 'sap_het_han' | 'con_han'."""
        n = self.so_ngay_con_han(hom_nay)
        if n is None:
            return "khong_han"
        if n < 0:
            return "het_han"
        if n <= self.NGAY_CANH_BAO_HET_HAN:
            return "sap_het_han"
        return "con_han"

    def to_dict(self):
        return {"ma": self.ma, "ten": self.ten, "loai": self.loai, "don_vi": self.don_vi,
                "so_luong": self.so_luong, "don_gia": self.don_gia, "han_su_dung": self.han_su_dung}

    def __str__(self):
        return f"{self.ma} - {self.ten} ({dinh_dang_so(self.so_luong)} {self.don_vi})"


class NguyenLieuTuoiSong(NguyenLieu):
    """Lớp con: nguyên liệu tươi sống (thịt, cá, rau...) - hạn ngắn nên cảnh báo sớm theo ngày."""
    NHOM = "Tươi sống"
    NGAY_CANH_BAO_HET_HAN = 3


LOAI_TUOI_SONG = {"thịt", "cá", "hải sản", "rau", "củ quả", "trứng", "sữa"}


def tao_nguyen_lieu(ma, ten, loai, don_vi, so_luong, don_gia, han_su_dung=""):
    """Factory: chọn lớp phù hợp theo loại nguyên liệu (đa hình)."""
    lop = NguyenLieuTuoiSong if str(loai).strip().lower() in LOAI_TUOI_SONG else NguyenLieu
    return lop(ma, ten, loai, don_vi, so_luong, don_gia, han_su_dung)


class QuanLyNguyenLieu:
    def __init__(self, kho):
        self.kho = kho

    def tim_theo_ma(self, ma):
        ma = str(ma).strip().upper()
        for nl in self.kho.nguyen_lieu:
            if nl.ma == ma:
                return nl
        return None

    def lay_nguyen_lieu(self, ma):
        nl = self.tim_theo_ma(ma)
        if nl is None:
            raise LoiKho("Không tìm thấy nguyên liệu!")
        return nl

    def them_nguyen_lieu(self, ma, ten, loai, don_vi, so_luong, don_gia, han_su_dung=""):
        nl = tao_nguyen_lieu(ma, ten, loai, don_vi, so_luong, don_gia, han_su_dung)  # kiểm tra dữ liệu ở đây
        if self.tim_theo_ma(nl.ma):
            raise LoiKho("Mã nguyên liệu đã tồn tại!")
        self.kho.nguyen_lieu.append(nl)
        return nl

    def hien_thi_danh_sach(self, danh_sach=None):
        ds = self.kho.nguyen_lieu if danh_sach is None else danh_sach
        if not ds:
            print("(Không có nguyên liệu nào)")
            return
        print(f"{'STT':<4}{'Mã':<7}{'Tên':<16}{'Loại':<11}{'ĐV':<6}{'Số lượng':>9}{'Đơn giá':>11}  {'HSD':<11}")
        print("-" * 78)
        for i, nl in enumerate(ds, 1):
            print(f"{i:<4}{nl.ma:<7}{nl.ten:<16}{nl.loai:<11}{nl.don_vi:<6}"
                  f"{dinh_dang_so(nl.so_luong):>9}{dinh_dang_tien(nl.don_gia):>11}  {nl.han_su_dung or '-':<11}")

    def tim_nguyen_lieu(self, tu_khoa):
        tu_khoa = str(tu_khoa).strip().lower()
        if not tu_khoa:
            raise LoiKho("Từ khóa tìm kiếm không được để trống!")
        return [nl for nl in self.kho.nguyen_lieu
                if tu_khoa in nl.ma.lower() or tu_khoa in nl.ten.lower() or tu_khoa in nl.loai.lower()]

    def sua_nguyen_lieu(self, ma, **thay_doi):
        cu = self.lay_nguyen_lieu(ma)
        du_lieu = cu.to_dict()
        du_lieu.update({k: v for k, v in thay_doi.items() if v not in (None, "")})
        du_lieu["ma"] = cu.ma  # không cho đổi mã
        moi = tao_nguyen_lieu(**du_lieu)  # sai dữ liệu -> ném LoiKho, bản cũ giữ nguyên
        self.kho.nguyen_lieu[self.kho.nguyen_lieu.index(cu)] = moi
        return moi

    def xoa_nguyen_lieu(self, ma):
        self.kho.nguyen_lieu.remove(self.lay_nguyen_lieu(ma))


def menu_nguyen_lieu(kho):
    ql = QuanLyNguyenLieu(kho)
    while True:
        print("\n===== QUẢN LÝ NGUYÊN LIỆU =====")
        print("1. Thêm nguyên liệu\n2. Hiển thị nguyên liệu\n3. Tìm kiếm\n"
              "4. Sửa nguyên liệu\n5. Xóa nguyên liệu\n0. Quay lại")
        chon = input("Chọn: ").strip()
        try:
            if chon == "1":
                ma = input("Mã: ")
                ten = input("Tên: ")
                loai = input("Loại: ")
                don_vi = input("Đơn vị: ")
                sl = input("Số lượng: ")
                gia = input("Đơn giá: ")
                hsd = input("Hạn sử dụng (dd/mm/yyyy, Enter nếu không có): ")
                ql.them_nguyen_lieu(ma, ten, loai, don_vi, sl, gia, hsd)
                kho.luu()
                print("✓ Thêm nguyên liệu thành công!")
            elif chon == "2":
                ql.hien_thi_danh_sach()
            elif chon == "3":
                ql.hien_thi_danh_sach(ql.tim_nguyen_lieu(input("Nhập mã/tên cần tìm: ")))
            elif chon == "4":
                ma = input("Mã nguyên liệu cần sửa: ")
                nl = ql.lay_nguyen_lieu(ma)
                print(f"Đang sửa: {nl}  (Enter để giữ nguyên)")
                ql.sua_nguyen_lieu(ma, ten=input("Tên mới: "), loai=input("Loại mới: "),
                                   don_vi=input("Đơn vị mới: "), so_luong=input("Số lượng mới: "),
                                   don_gia=input("Đơn giá mới: "), han_su_dung=input("Hạn sử dụng mới: "))
                kho.luu()
                print("✓ Sửa nguyên liệu thành công!")
            elif chon == "5":
                ma = input("Mã nguyên liệu cần xóa: ")
                ql.xoa_nguyen_lieu(ma)
                kho.luu()
                print("✓ Xóa nguyên liệu thành công!")
            elif chon == "0":
                return
            else:
                print("✗ Lựa chọn không hợp lệ!")
        except LoiKho as e:
            print(f"✗ {e}")
