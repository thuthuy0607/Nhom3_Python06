```python
from datetime import datetime

# Danh sach phieu xuat
danh_sach_phieu_xuat = []


# 1. Tao phieu xuat
def tao_phieu_xuat():
    """Tao phieu xuat kho moi."""

    ma_phieu = input("Nhap ma phieu xuat: ").strip().upper()

    if not ma_phieu:
        print("Ma phieu khong duoc de trong!")
        return None

    # Kiem tra trung ma phieu
    for phieu in danh_sach_phieu_xuat:
        if phieu["ma_phieu"] == ma_phieu:
            print("Ma phieu xuat da ton tai!")
            return None

    ngay_xuat = datetime.now().strftime("%d/%m/%Y")

    phieu_xuat = {
        "ma_phieu": ma_phieu,
        "ngay_xuat": ngay_xuat,
        "muc_dich": "",
        "chi_tiet": []
    }

    danh_sach_phieu_xuat.append(phieu_xuat)

    print("\nTao phieu xuat thanh cong!")
    print("Ma phieu:", ma_phieu)
    print("Ngay xuat:", ngay_xuat)

    return phieu_xuat


# 2. Kiem tra so luong
def kiem_tra_so_luong(nguyen_lieu, so_luong_xuat):
    """Kiem tra so luong xuat co hop le khong."""

    if so_luong_xuat <= 0:
        print("So luong xuat phai lon hon 0!")
        return False

    if so_luong_xuat > nguyen_lieu["so_luong"]:
        print("Khong du nguyen lieu trong kho!")
        print("So luong ton:", nguyen_lieu["so_luong"],
              nguyen_lieu["don_vi"])
        return False

    return True


# 3. Cap nhat ton kho
def cap_nhat_ton_kho(danh_sach_nguyen_lieu, ma, so_luong_xuat):
    """Tru so luong nguyen lieu sau khi xuat."""

    for nguyen_lieu in danh_sach_nguyen_lieu:
        if nguyen_lieu["ma"] == ma:
            if so_luong_xuat <= 0:
                return False

            if so_luong_xuat > nguyen_lieu["so_luong"]:
                return False

            nguyen_lieu["so_luong"] -= so_luong_xuat
            return True

    return False


# 4. Them chi tiet xuat
def them_chi_tiet_xuat(phieu_xuat, danh_sach_nguyen_lieu):
    """Them nguyen lieu vao phieu xuat."""

    if phieu_xuat is None:
        print("Phieu xuat khong hop le!")
        return

    ma = input("Nhap ma nguyen lieu: ").strip().upper()

    # Tim nguyen lieu
    nguyen_lieu_tim_thay = None

    for nguyen_lieu in danh_sach_nguyen_lieu:
        if nguyen_lieu["ma"] == ma:
            nguyen_lieu_tim_thay = nguyen_lieu
            break

    if nguyen_lieu_tim_thay is None:
        print("Khong tim thay nguyen lieu!")
        return

    # Nhap so luong xuat
    try:
        so_luong_xuat = float(
            input("Nhap so luong xuat: ")
        )

        if not kiem_tra_so_luong(
            nguyen_lieu_tim_thay,
            so_luong_xuat
        ):
            return

    except ValueError:
        print("So luong phai la mot so hop le!")
        return

    muc_dich = input(
        "Nhap muc dich xuat kho: "
    ).strip()

    if not muc_dich:
        muc_dich = "Su dung trong quan an"

    # Cap nhat ton kho
    if cap_nhat_ton_kho(
        danh_sach_nguyen_lieu,
        ma,
        so_luong_xuat
    ):
        chi_tiet = {
            "ma": ma,
            "ten": nguyen_lieu_tim_thay["ten"],
            "so_luong": so_luong_xuat,
            "don_vi": nguyen_lieu_tim_thay["don_vi"],
            "muc_dich": muc_dich
        }

        phieu_xuat["chi_tiet"].append(chi_tiet)
        phieu_xuat["muc_dich"] = muc_dich

        print("\n===== XUAT KHO THANH CONG =====")
        print("Ten nguyen lieu:",
              nguyen_lieu_tim_thay["ten"])
        print("So luong xuat:",
              so_luong_xuat,
              nguyen_lieu_tim_thay["don_vi"])
        print("Muc dich:", muc_dich)
        print("Ton kho sau xuat:",
              nguyen_lieu_tim_thay["so_luong"],
              nguyen_lieu_tim_thay["don_vi"])

    else:
        print("Khong the xuat kho!")


# 5. Hien thi phieu xuat
def hien_thi_phieu_xuat():
    """Hien thi danh sach phieu xuat."""

    if not danh_sach_phieu_xuat:
        print("Chua co phieu xuat nao!")
        return

    print("\n========== DANH SACH PHIEU XUAT ==========")

    for phieu in danh_sach_phieu_xuat:
        print("\nMa phieu:", phieu["ma_phieu"])
        print("Ngay xuat:", phieu["ngay_xuat"])

        if not phieu["chi_tiet"]:
            print("Phieu xuat chua co nguyen lieu.")
        else:
            for chi_tiet in phieu["chi_tiet"]:
                print("------------------------------")
                print("Ma nguyen lieu:", chi_tiet["ma"])
                print("Ten nguyen lieu:", chi_tiet["ten"])
                print("So luong:", chi_tiet["so_luong"],
                      chi_tiet["don_vi"])
                print("Muc dich:", chi_tiet["muc_dich"])

        print("------------------------------")


# 6. Menu xuat kho
def menu_xuat_kho(danh_sach_nguyen_lieu):
    """Menu dieu khien chuc nang xuat kho."""

    while True:
        print("\n========== QUAN LY XUAT KHO ==========")
        print("1. Tao phieu xuat")
        print("2. Them nguyen lieu vao phieu xuat")
        print("3. Hien thi danh sach phieu xuat")
        print("0. Quay lai menu chinh")

        chon = input("Nhap lua chon: ").strip()

        if chon == "1":
            tao_phieu_xuat()

        elif chon == "2":
            if not danh_sach_phieu_xuat:
                print("Vui long tao phieu xuat truoc!")
                continue

            ma_phieu = input(
                "Nhap ma phieu xuat: "
            ).strip().upper()

            phieu_tim_thay = None

            for phieu in danh_sach_phieu_xuat:
                if phieu["ma_phieu"] == ma_phieu:
                    phieu_tim_thay = phieu
                    break

            if phieu_tim_thay is None:
                print("Khong tim thay phieu xuat!")
            else:
                them_chi_tiet_xuat(
                    phieu_tim_thay,
                    danh_sach_nguyen_lieu
                )

        elif chon == "3":
            hien_thi_phieu_xuat()

        elif chon == "0":
            print("Quay lai menu chinh!")
            break

        else:
            print("Lua chon khong hop le!")
```

