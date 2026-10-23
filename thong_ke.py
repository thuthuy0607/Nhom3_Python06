
from du_lieu import lay_danh_sach_nl
from datetime import datetime, date

# Nguong canh bao
NGUONG_SAP_HET = 5
NGAY_CANH_BAO_HAN = 7


def thong_ke_nguyen_lieu():
    """Thong ke tong so nguyen lieu, con hang, sap het va het hang."""
    ds = lay_danh_sach_nl()

    tong = len(ds)
    con_hang = sum(1 for x in ds if x["so_luong"] > 0)
    sap_het = sum(
        1 for x in ds
        if 0 < x["so_luong"] <= NGUONG_SAP_HET
    )
    het_hang = sum(1 for x in ds if x["so_luong"] == 0)

    print("\n===== THONG KE NGUYEN LIEU =====")
    print(f"Tong so nguyen lieu: {tong}")
    print(f"Nguyen lieu con hang: {con_hang}")
    print(f"Nguyen lieu sap het (<= {NGUONG_SAP_HET}): {sap_het}")
    print(f"Nguyen lieu da het hang: {het_hang}")


def tinh_gia_tri_ton_kho():
    """Tinh tong gia tri ton kho theo so luong nhan don gia."""
    ds = lay_danh_sach_nl()
    tong_gia_tri = 0

    print("\n===== GIA TRI TON KHO =====")
    for nl in ds:
        gia_tri = nl["so_luong"] * nl["don_gia"]
        tong_gia_tri += gia_tri
        print(
            f"{nl['ten']}: {nl['so_luong']} x "
            f"{nl['don_gia']:,.0f} = {gia_tri:,.0f} VND"
        )

    print(f"\n=> TONG GIA TRI KHO: {tong_gia_tri:,.0f} VND")


def canh_bao_ton_kho():
    """Canh bao nguyen lieu sap het hoac da het hang."""
    ds = lay_danh_sach_nl()
    print("\n===== CANH BAO TON KHO =====")
    co_canh_bao = False

    for nl in ds:
        so_luong = nl["so_luong"]

        if so_luong == 0:
            print(
                f"[HET HANG] {nl['ten']} ({nl['ma']}): "
                "Da het! Can nhap them ngay."
            )
            co_canh_bao = True
        elif 0 < so_luong <= NGUONG_SAP_HET:
            print(
                f"[SAP HET] {nl['ten']} ({nl['ma']}): "
                f"con {so_luong} {nl['don_vi']}"
            )
            co_canh_bao = True

    if not co_canh_bao:
        print("Khong co nguyen lieu nao sap het. Ton kho dang tot.")


def kiem_tra_han_su_dung():
    """Canh bao nguyen lieu da het han hoac sap het han trong 7 ngay."""
    ds = lay_danh_sach_nl()
    hom_nay = date.today()
    print("\n===== KIEM TRA HAN SU DUNG =====")
    co_canh_bao = False

    for nl in ds:
        try:
            han = datetime.strptime(
                nl["han_su_dung"], "%d/%m/%Y"
            ).date()
            so_ngay = (han - hom_nay).days

            if so_ngay < 0:
                print(
                    f"[DA HET HAN] {nl['ten']} ({nl['ma']}): "
                    f"het han ngay {nl['han_su_dung']}. Khong duoc su dung!"
                )
                co_canh_bao = True
            elif so_ngay <= NGAY_CANH_BAO_HAN:
                print(
                    f"[SAP HET HAN] {nl['ten']} ({nl['ma']}): "
                    f"con {so_ngay} ngay (den {nl['han_su_dung']})"
                )
                co_canh_bao = True

        except (ValueError, TypeError):
            print(
                f"[LOI DINH DANG] {nl.get('ten', 'Nguyen lieu')}: "
                "Han su dung khong hop le!"
            )
            co_canh_bao = True

    if not co_canh_bao:
        print("Tat ca nguyen lieu con han su dung tot.")


def menu_thong_ke():
    """Menu rieng cho cac chuc nang thong ke va canh bao."""
    while True:
        print("\n===== THONG KE + CANH BAO =====")
        print("1. Thong ke nguyen lieu")
        print("2. Tinh gia tri ton kho")
        print("3. Canh bao ton kho sap het")
        print("4. Kiem tra han su dung")
        print("0. Quay lai menu chinh")

        chon = input("Chon chuc nang: ").strip()

        if chon == "1":
            thong_ke_nguyen_lieu()
        elif chon == "2":
            tinh_gia_tri_ton_kho()
        elif chon == "3":
            canh_bao_ton_kho()
        elif chon == "4":
            kiem_tra_han_su_dung()

