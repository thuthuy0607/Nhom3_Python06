from datetime import datetime

from ngoai_le import (
    DuLieuKhongHopLe,
    NguyenLieuDaTonTai,
    NguyenLieuKhongTonTai,
)

class NguyenLieu:
    def __init__(self, ma, ten, loai, don_vi, so_luong, don_gia, han_su_dung):
        self.ma = ma
        self.ten = ten
        self.loai = loai
        self.don_vi = don_vi
        self.so_luong = so_luong
        self.don_gia = don_gia
        self.han_su_dung = han_su_dung

    @property
    def ma(self):
        return self.__ma

    @ma.setter
    def ma(self, gia_tri):
        gia_tri = str(gia_tri).strip()
        if not gia_tri:
            raise DuLieuKhongHopLe("Mã nguyên liệu không được để trống!")
        self.__ma = gia_tri

    @property
    def ten(self):
        return self.__ten

    @ten.setter
    def ten(self, gia_tri):
        gia_tri = str(gia_tri).strip()
        if not gia_tri:
            raise DuLieuKhongHopLe("Tên nguyên liệu không được để trống!")
        self.__ten = gia_tri

    @property
    def loai(self):
        return self.__loai

    @loai.setter
    def loai(self, gia_tri):
        gia_tri = str(gia_tri).strip()
        if not gia_tri:
            raise DuLieuKhongHopLe("Loại nguyên liệu không được để trống!")
        self.__loai = gia_tri

    @property
    def don_vi(self):
        return self.__don_vi

    @don_vi.setter
    def don_vi(self, gia_tri):
        gia_tri = str(gia_tri).strip()
        if not gia_tri:
            raise DuLieuKhongHopLe("Đơn vị tính không được để trống!")
        self.__don_vi = gia_tri

    @property
    def so_luong(self):
        return self.__so_luong

    @so_luong.setter
    def so_luong(self, gia_tri):
        try:
            gia_tri = float(gia_tri)
        except (TypeError, ValueError):
            raise DuLieuKhongHopLe("Số lượng phải là số!") from None
        if gia_tri < 0:
            raise DuLieuKhongHopLe("Số lượng không được âm!")
        self.__so_luong = gia_tri

    @property
    def don_gia(self):
        return self.__don_gia

    @don_gia.setter
    def don_gia(self, gia_tri):
        try:
            gia_tri = float(gia_tri)
        except (TypeError, ValueError):
            raise DuLieuKhongHopLe("Đơn giá phải là số!") from None
        if gia_tri < 0:
            raise DuLieuKhongHopLe("Đơn giá không được âm!")
        self.__don_gia = gia_tri

    @property
    def han_su_dung(self):
        return self.__han_su_dung

    @han_su_dung.setter
    def han_su_dung(self, gia_tri):
        gia_tri = str(gia_tri).strip()
        try:
            datetime.strptime(gia_tri, "%d/%m/%Y")
        except ValueError:
            raise DuLieuKhongHopLe(
            ) from None
        self.__han_su_dung = gia_tri

    def to_dict(self):
        #Chuyển đối tượng nguyên liệu thành dictionary để lưu JSON.
        return {
            "ma": self.ma,
            "ten": self.ten,
            "loai": self.loai,
            "don_vi": self.don_vi,
            "so_luong": self.so_luong,
            "don_gia": self.don_gia,
            "han_su_dung": self.han_su_dung,
        }

    @classmethod
    def from_dict(cls, du_lieu):
        #Tạo đối tượng NguyenLieu từ một dictionary đọc từ JSON.
        cac_truong = (
            "ma", "ten", "loai", "don_vi",
            "so_luong", "don_gia", "han_su_dung",
        )
        thieu = [truong for truong in cac_truong if truong not in du_lieu]
        if thieu:
            raise DuLieuKhongHopLe(
                "Dữ liệu thiếu trường: " + ", ".join(thieu)
            )
        return cls(**{truong: du_lieu[truong] for truong in cac_truong})

    def __str__(self):
        #Trả về thông tin nguyên liệu ở dạng dễ đọc.
        return (
            f"Mã: {self.ma} | Tên: {self.ten} | Loại: {self.loai} | "
            f"Đơn vị: {self.don_vi} | Số lượng: {self.so_luong:g} | "
            f"Đơn giá: {self.don_gia:,.0f} VNĐ | "
            f"Hạn sử dụng: {self.han_su_dung}"
        )


class QuanLyNguyenLieu:
    def __init__(self, danh_sach=None):
        self.danh_sach = []
        for item in danh_sach or []:
            if isinstance(item, NguyenLieu):
                self.danh_sach.append(item)
            elif isinstance(item, dict):
                self.danh_sach.append(NguyenLieu.from_dict(item))
            else:
                raise DuLieuKhongHopLe(
                    "Danh sách chỉ nhận NguyenLieu hoặc dictionary!"
                )

    def them_nguyen_lieu(self, nguyen_lieu):
        if isinstance(nguyen_lieu, dict):
            nguyen_lieu = NguyenLieu.from_dict(nguyen_lieu)
        if not isinstance(nguyen_lieu, NguyenLieu):
            raise DuLieuKhongHopLe("Dữ liệu thêm phải là đối tượng NguyenLieu!")
        if self.tim_theo_ma(nguyen_lieu.ma) is not None:
            raise NguyenLieuDaTonTai(
                f"Mã nguyên liệu {nguyen_lieu.ma} đã tồn tại!"
            )
        self.danh_sach.append(nguyen_lieu)
        return nguyen_lieu

    def hien_thi_danh_sach(self):
        return list(self.danh_sach)

    def tim_theo_ma(self, ma):
        #Tìm một nguyên liệu theo mã; trả về None nếu không có.
        ma = str(ma).strip().lower()
        for nguyen_lieu in self.danh_sach:
            if nguyen_lieu.ma.lower() == ma:
                return nguyen_lieu
        return None

    def tim_nguyen_lieu(self, tu_khoa):
        #Tìm nguyên liệu theo một phần mã hoặc tên, không phân biệt hoa thường.
        tu_khoa = str(tu_khoa).strip().lower()
        if not tu_khoa:
            return []
        return [
            item for item in self.danh_sach
            if tu_khoa in item.ma.lower() or tu_khoa in item.ten.lower()
        ]

    def sua_nguyen_lieu(self, ma, **thay_doi):
        nguyen_lieu = self.tim_theo_ma(ma)
        if nguyen_lieu is None:
            raise NguyenLieuKhongTonTai(
                f"Không tìm thấy nguyên liệu có mã {ma}!"
            )

        cac_truong_hop_le = {
            "ten", "loai", "don_vi", "so_luong", "don_gia", "han_su_dung"
        }
        truong_khong_hop_le = set(thay_doi) - cac_truong_hop_le
        if truong_khong_hop_le:
            raise DuLieuKhongHopLe(
                "Trường không được phép sửa: "
                + ", ".join(sorted(truong_khong_hop_le))
            )

        # Kiểm tra trên một bản sao trước để tránh cập nhật dở dang nếu dữ liệu sai.
        du_lieu_moi = nguyen_lieu.to_dict()
        du_lieu_moi.update(thay_doi)
        nguyen_lieu_moi = NguyenLieu.from_dict(du_lieu_moi)

        nguyen_lieu.ten = nguyen_lieu_moi.ten
        nguyen_lieu.loai = nguyen_lieu_moi.loai
        nguyen_lieu.don_vi = nguyen_lieu_moi.don_vi
        nguyen_lieu.so_luong = nguyen_lieu_moi.so_luong
        nguyen_lieu.don_gia = nguyen_lieu_moi.don_gia
        nguyen_lieu.han_su_dung = nguyen_lieu_moi.han_su_dung
        return nguyen_lieu

    def xoa_nguyen_lieu(self, ma):
        nguyen_lieu = self.tim_theo_ma(ma)
        if nguyen_lieu is None:
            raise NguyenLieuKhongTonTai(
                f"Không tìm thấy nguyên liệu có mã {ma}!"
            )
        self.danh_sach.remove(nguyen_lieu)
        return nguyen_lieu


def menu_nguyen_lieu(quan_ly):
    while True:
        print("\n===== QUẢN LÝ NGUYÊN LIỆU =====")
        print("1. Thêm nguyên liệu")
        print("2. Hiển thị danh sách")
        print("3. Tìm kiếm nguyên liệu")
        print("4. Sửa nguyên liệu")
        print("5. Xóa nguyên liệu")
        print("0. Quay lại")

        lua_chon = input("Chọn chức năng: ").strip()

        try:
            if lua_chon == "1":
                nguyen_lieu = NguyenLieu(
                    input("Mã nguyên liệu: "),
                    input("Tên nguyên liệu: "),
                    input("Loại nguyên liệu: "),
                    input("Đơn vị tính: "),
                    input("Số lượng: "),
                    input("Đơn giá: "),
                    input("Hạn sử dụng (dd/mm/yyyy): "),
                )
                quan_ly.them_nguyen_lieu(nguyen_lieu)
                print("Thêm nguyên liệu thành công!")

            elif lua_chon == "2":
                danh_sach = quan_ly.hien_thi_danh_sach()
                if not danh_sach:
                    print("Danh sách nguyên liệu đang trống!")
                else:
                    for item in danh_sach:
                        print(item)

            elif lua_chon == "3":
                tu_khoa = input("Nhập mã hoặc tên cần tìm: ")
                ket_qua = quan_ly.tim_nguyen_lieu(tu_khoa)
                if ket_qua:
                    for item in ket_qua:
                        print(item)
                else:
                    print("Không tìm thấy nguyên liệu!")

            elif lua_chon == "4":
                ma = input("Nhập mã nguyên liệu cần sửa: ")
                if quan_ly.tim_theo_ma(ma) is None:
                    raise NguyenLieuKhongTonTai(
                        f"Không tìm thấy nguyên liệu có mã {ma}!"
                    )
                print("Nhập thông tin mới:")
                quan_ly.sua_nguyen_lieu(
                    ma,
                    ten=input("Tên mới: "),
                    loai=input("Loại mới: "),
                    don_vi=input("Đơn vị mới: "),
                    so_luong=input("Số lượng mới: "),
                    don_gia=input("Đơn giá mới: "),
                    han_su_dung=input("Hạn sử dụng mới (dd/mm/yyyy): "),
                )
                print("Sửa nguyên liệu thành công!")

            elif lua_chon == "5":
                ma = input("Nhập mã nguyên liệu cần xóa: ")
                nguyen_lieu = quan_ly.tim_theo_ma(ma)
                if nguyen_lieu is None:
                    raise NguyenLieuKhongTonTai(
                        f"Không tìm thấy nguyên liệu có mã {ma}!"
                    )
                print(nguyen_lieu)
                xac_nhan = input("Bạn có chắc muốn xóa? (y/n): ").strip().lower()
                if xac_nhan == "y":
                    quan_ly.xoa_nguyen_lieu(ma)
                    print("Xóa nguyên liệu thành công!")
                else:
                    print("Đã hủy xóa.")

            elif lua_chon == "0":
                print("Đã thoát quản lý nguyên liệu.")
                break

            else:
                print("Lựa chọn không hợp lệ!")

        except (DuLieuKhongHopLe, NguyenLieuDaTonTai, NguyenLieuKhongTonTai) as loi:
            print("Lỗi:", loi)


if __name__ == "__main__":
    quan_ly = QuanLyNguyenLieu()
    menu_nguyen_lieu(quan_ly)
