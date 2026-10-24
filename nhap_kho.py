```python
from datetime import datetime

# Danh sach phieu nhap
danh_sach_phieu_nhap = []


# 1. Tao phieu nhap
def tao_phieu_nhap():
    """Tao mot phieu nhap kho moi."""

    ma_phieu = input("Nhap ma phieu nhap: ").strip().upper()

    if not ma_phieu:
        print("Ma phieu khong duoc de trong!")
        return None

    # Kiem tra trung ma phieu
    for phieu in danh_sach_phieu_nhap:
        if phieu["ma_phieu"] == ma_phieu:
            print("Ma phieu nhap da ton tai!")
            return None

    ngay_nhap = datetime.now().strftime("%d/%m/%Y")

    phieu_nhap = {
        "ma_phieu": ma_phieu,
        "ngay_nhap": ngay_nhap,
        "chi_tiet": [],
        "tong_tien": 0
    }

    danh_sach_phieu_nhap.append(phieu_nhap)

    print("Tao phieu nhap thanh cong!")
    print("Ma phieu:", ma_phieu)
    print("Ngay nhap:", ngay_nhap)

    return phieu_nhap


# 2. Tinh tien nhap
def tinh_tien_nhap(so_luong, don_gia):
    """Tinh thanh tien cua mot nguyen lieu."""

    return so_luong * don_gia


# 3. Cap nhat ton kho
def cap_nhat_ton_kho(danh_sach_nguyen_lieu, ma, so_luong):
    """Cong so luong nhap vao ton kho."""

    for nguyen_lieu in danh_sach_nguyen_lieu:
        if nguyen_lieu["ma"] == ma:
            nguyen_lieu["so_luong"] += so_luong
            return True

    return False


# 4. Them chi tiet nhap
def them_chi_tiet_nhap(phieu_nhap, danh_sach_nguyen_lieu):
    """Them mot nguyen lieu vao phieu nhap."""

    if phieu_nhap is None:
        print("Phieu nhap khong hop le!")
        return

    ma = input("Nhap ma nguyen lieu: ").strip().upper()

    # Tim nguyen lieu trong danh sach
    nguyen_lieu_tim_thay = None

    for nguyen_lieu in danh_sach_nguyen_lieu:
        if nguyen_lieu["ma"] == ma:
            nguyen_lieu_tim_thay = nguyen_lieu
            break

    if nguyen_lieu_tim_thay is None:
        print("Khong tim thay nguyen lieu!")
        return

    # Nhap so luong
    try:
        so_luong = float(input("Nhap so luong nhap: "))

        if so_luong <= 0:
            print("So luong nhap phai lon hon 0!")
            return

        # Nhap don gia
        don_gia = float(input("Nhap don gia: "))

        if don_gia <= 0:
            print("Don gia phai lon hon 0!")
            return

    except ValueError:
        print("Vui long nhap so hop le!")
        return

    # Tinh thanh tien
    thanh_tien = tinh_tien_nhap(so_luong, don_gia)

    # Tao chi tiet phieu nhap
    chi_tiet = {
        "ma": ma,
        "ten": nguyen_lieu["ten"],
        "so_luong": so_luong,
        "don_vi": nguyen_lieu["don_vi"],
        "don_gia": don_gia,
        "thanh_tien": thanh_tien
    }

    # Cap nhat ton kho
    if cap_nhat_ton_kho(
        danh_sach_nguyen_lieu,
        ma,
        so_luong
    ):
        phieu_nhap["chi_tiet"].append(chi_tiet)
        phieu_nhap["tong_tien"] += thanh_tien

        print("\n===== NHAP KHO THANH CONG =====")
        print("Ten nguyen lieu:", nguyen_lieu_tim_thay["ten"])
        print("So luong nhap:", so_luong,
              nguyen_lieu_tim_thay["don_vi"])
        print("Don gia:", f"{don_gia:,.0f}", "VNĐ")
        print("Thanh tien:", f"{thanh_tien:,.0f}", "VNĐ")
        print(
            "Ton kho hien tai:",
            nguyen_lieu_tim_thay["so_luong"],
            nguyen_lieu_tim_thay["don_vi"]
        )
    else:
        print("Khong the cap nhat ton kho!")


# 5. Hien thi phieu nhap
def hien_thi_phieu_nhap():
    """Hien thi danh sach phieu nhap kho."""

    if not danh_sach_phieu_nhap:
        print("Chua co phieu nhap nao!")
        return

    print("\n========== DANH SACH PHIEU NHAP ==========")

    for phieu in danh_sach_phieu_nhap:
        print("\nMa phieu:", phieu["ma_phieu"])
        print("Ngay nhap:", phieu["ngay_nhap"])

        if not phieu["chi_tiet"]:
            print("Phieu nhap chua co nguyen lieu.")
        else:
            print("------------------------------------------")

            for ct in phieu["chi_tiet"]:
                print("Ma nguyen lieu:", ct["ma"])
                print("Ten nguyen lieu:", ct["ten"])
                print("So luong:", ct["so_luong"], ct["don_vi"])
                print("Don gia:", f"{ct['don_gia']:,.0f}", "VNĐ")
                print("Thanh tien:", f"{ct['thanh_tien']:,.0f}", "VNĐ")
                print("------------------------------------------")

        print("Tong tien phieu nhap:",
              f"{phieu['tong_tien']:,.0f}", "VNĐ")


# 6. Menu nhap kho
def menu_nhap_kho(danh_sach_nguyen_lieu):
    """Menu dieu khien chuc nang nhap kho."""

    while True:
        print("\n========== QUAN LY NHAP KHO ==========")
        print("1. Tao phieu nhap")
        print("2. Them nguyen lieu vao phieu nhap")
        print("3. Hien thi danh sach phieu nhap")
        print("0. Quay lai")

        chon = input("Nhap lua chon: ").strip()

        if chon == "1":
            tao_phieu_nhap()

        elif chon == "2":
            if not danh_sach_phieu_nhap:
                print("Vui long tao phieu nhap truoc!")
                continue

            ma_phieu = input("Nhap ma phieu nhap: ").strip().upper()

            phieu_tim_thay = None

            for phieu in danh_sach_phieu_nhap:
                if phieu["ma_phieu"] == ma_phieu:
                    phieu_tim_thay = phieu
                    break

            if phieu_tim_thay is None:
                print("Khong tim thay phieu nhap!")
            else:
                them_chi_tiet_nhap(
                    phieu_tim_thay,
                    danh_sach_nguyen_lieu
                )

        elif chon == "3":
            hien_thi_phieu_nhap()

        elif chon == "0":
            print("Quay lai menu chinh!")
            break

        else:
            print("Lua chon khong hop le!")


