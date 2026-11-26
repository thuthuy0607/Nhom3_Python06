"""du_lieu.py - Đọc/ghi dữ liệu JSON, hàm dùng chung, lớp lỗi riêng (cả nhóm phối hợp)."""
import json
import os
from datetime import datetime

DINH_DANG_NGAY = "%d/%m/%Y"
DUONG_DAN_MAC_DINH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")


class LoiKho(Exception):
    """Lỗi nghiệp vụ của chương trình quản lý kho (dữ liệu sai, không tìm thấy, không đủ hàng...)."""


def chuyen_ngay(chuoi):
    """Chuyển chuỗi dd/mm/yyyy thành đối tượng date; sai định dạng -> LoiKho."""
    try:
        return datetime.strptime(str(chuoi).strip(), DINH_DANG_NGAY).date()
    except ValueError:
        raise LoiKho("Ngày không hợp lệ (đúng định dạng dd/mm/yyyy)!")


def doc_so(chuoi, ten_truong):
    """Chuyển chuỗi thành số thực; không phải số -> LoiKho."""
    try:
        return float(str(chuoi).strip().replace(",", "."))
    except ValueError:
        raise LoiKho(f"{ten_truong} phải là số!")


def dinh_dang_so(x):
    x = float(x)
    return str(int(x)) if x.is_integer() else str(round(x, 2))


def dinh_dang_tien(x):
    return f"{float(x):,.0f}".replace(",", ".")


class KhoDuLieu:
    """Giữ toàn bộ dữ liệu trong bộ nhớ và đồng bộ với file data.json."""

    def __init__(self, duong_dan=DUONG_DAN_MAC_DINH):
        self.duong_dan = duong_dan
        self.nguyen_lieu = []   # list[NguyenLieu]
        self.phieu_nhap = []    # list[dict]
        self.phieu_xuat = []    # list[dict]

    def doc(self):
        from nguyen_lieu import tao_nguyen_lieu  # import trễ để tránh vòng lặp import
        try:
            with open(self.duong_dan, "r", encoding="utf-8") as f:
                du_lieu = json.load(f)
        except FileNotFoundError:
            self.luu()
            return
        except json.JSONDecodeError:
            sao_luu = self.duong_dan + ".loi"
            os.replace(self.duong_dan, sao_luu)
            print(f"⚠️ File dữ liệu bị hỏng, đã đổi tên thành {os.path.basename(sao_luu)}. Bắt đầu với kho trống.")
            self.luu()
            return
        except OSError as e:
            raise LoiKho(f"Không đọc được file dữ liệu: {e}")

        self.nguyen_lieu = []
        for d in du_lieu.get("nguyen_lieu", []):
            try:
                self.nguyen_lieu.append(tao_nguyen_lieu(**d))
            except (LoiKho, TypeError) as e:
                print(f"⚠️ Bỏ qua một bản ghi nguyên liệu lỗi: {e}")
        self.phieu_nhap = du_lieu.get("phieu_nhap", [])
        self.phieu_xuat = du_lieu.get("phieu_xuat", [])

    def luu(self):
        du_lieu = {
            "nguyen_lieu": [nl.to_dict() for nl in self.nguyen_lieu],
            "phieu_nhap": self.phieu_nhap,
            "phieu_xuat": self.phieu_xuat,
        }
        tam = self.duong_dan + ".tmp"
        try:
            with open(tam, "w", encoding="utf-8") as f:
                json.dump(du_lieu, f, ensure_ascii=False, indent=2)
            os.replace(tam, self.duong_dan)  # ghi an toàn: không mất dữ liệu cũ nếu lỗi giữa chừng
        except OSError as e:
            raise LoiKho(f"Không ghi được file dữ liệu: {e}")
