"""thong_ke.py - TV4: Thống kê kho, giá trị tồn, cảnh báo tồn kho và hạn sử dụng."""
from du_lieu import dinh_dang_so, dinh_dang_tien


class ThongKe:
    def __init__(self, kho, hom_nay=None):
        self.kho = kho
        self.hom_nay = hom_nay  # None = dùng ngày hiện tại (thư viện datetime)

    def thong_ke_nguyen_lieu(self):
        ds = self.kho.nguyen_lieu
        het_hang = [nl for nl in ds if nl.so_luong == 0]
        sap_het = [nl for nl in ds if 0 < nl.so_luong and nl.sap_het()]
        return {"tong": len(ds), "con_hang": len(ds) - len(het_hang) - len(sap_het),
                "sap_het": len(sap_het), "het_hang": len(het_hang)}

    def tinh_gia_tri_ton_kho(self):
        """Giá trị tồn = số lượng tồn x đơn giá. Trả về (danh sách (nl, giá trị), tổng)."""
        dong = [(nl, nl.gia_tri_ton()) for nl in self.kho.nguyen_lieu]
        return dong, sum(gt for _, gt in dong)

    def canh_bao_ton_kho(self):
        return [nl for nl in self.kho.nguyen_lieu if nl.sap_het()]

    def kiem_tra_han_su_dung(self):
        """Trả về list (nguyên liệu, trạng thái, số ngày còn lại) cho hàng đã/sắp hết hạn."""
        ket_qua = []
        for nl in self.kho.nguyen_lieu:
            tt = nl.trang_thai_han(self.hom_nay)
            if tt in ("het_han", "sap_het_han"):
                ket_qua.append((nl, tt, nl.so_ngay_con_han(self.hom_nay)))
        return ket_qua

    # ----- phần hiển thị -----
    def in_thong_ke(self):
        tk = self.thong_ke_nguyen_lieu()
        print("\n===== THỐNG KÊ KHO =====")
        print(f"Tổng số nguyên liệu: {tk['tong']}")
        print(f"Nguyên liệu còn hàng: {tk['con_hang']}")
        print(f"Nguyên liệu sắp hết: {tk['sap_het']}")
        print(f"Nguyên liệu hết hàng: {tk['het_hang']}")
        dong, tong = self.tinh_gia_tri_ton_kho()
        print("\n--- Giá trị tồn kho ---")
        for nl, gt in dong:
            print(f"{nl.ten}: {dinh_dang_so(nl.so_luong)} × {dinh_dang_tien(nl.don_gia)} = {dinh_dang_tien(gt)} VNĐ")
        print(f"TỔNG GIÁ TRỊ KHO: {dinh_dang_tien(tong)} VNĐ")

    def in_canh_bao_ton_kho(self):
        ds = self.canh_bao_ton_kho()
        print("\n===== CẢNH BÁO TỒN KHO =====")
        if not ds:
            print("✓ Không có nguyên liệu nào sắp hết.")
            return
        print("⚠️ CẢNH BÁO")
        for nl in ds:
            print(f"{nl.ten}: còn {dinh_dang_so(nl.so_luong)} {nl.don_vi}")

    def in_han_su_dung(self):
        ds = self.kiem_tra_han_su_dung()
        print("\n===== KIỂM TRA HẠN SỬ DỤNG =====")
        if not ds:
            print("✓ Không có nguyên liệu nào sắp hoặc đã hết hạn.")
            return
        for nl, tt, ngay in ds:
            if tt == "het_han":
                print(f"⚠️ {nl.ten} đã hết hạn! (HSD {nl.han_su_dung}, quá {-ngay} ngày)")
            else:
                print(f"⚠️ {nl.ten} sắp hết hạn! (HSD {nl.han_su_dung}, còn {ngay} ngày)")
