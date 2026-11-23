# Các ngoại lệ tùy chỉnh dùng trong ứng dụng quản lý kho nguyên liệu.

class KhoError(Exception):
    pass


class NguyenLieuKhongTonTai(KhoError):
    pass


class DuLieuKhongHopLe(KhoError):
    pass


class NguyenLieuDaTonTai(KhoError):
    pass
