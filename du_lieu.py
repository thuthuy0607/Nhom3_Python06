import json
from pathlib import Path

# File du lieu mac dinh cua chuong trinh quan ly kho.
# Cac module nguyen_lieu.py, nhap_kho.py, xuat_kho.py va thong_ke.py
# can thong nhat dung cung cau truc du lieu nay.

DUONG_DAN_DU_LIEU = Path(__file__).with_name("data.json")


def doc_du_lieu():
    """Doc du lieu tu data.json; neu chua co thi tao cau truc rong."""
    if not DUONG_DAN_DU_LIEU.exists():
        du_lieu = {"nguyen_lieu": [], "phieu_nhap": [], "phieu_xuat": []}
        ghi_du_lieu(du_lieu)
        return du_lieu

    try:
        with DUONG_DAN_DU_LIEU.open("r", encoding="utf-8") as tep:
            du_lieu = json.load(tep)
    except (json.JSONDecodeError, OSError):
        raise ValueError("Khong doc duoc data.json. Hay kiem tra noi dung file.")

    if not isinstance(du_lieu, dict):
        raise ValueError("Cau truc data.json khong hop le.")

    du_lieu.setdefault("nguyen_lieu", [])
    du_lieu.setdefault("phieu_nhap", [])
    du_lieu.setdefault("phieu_xuat", [])
    return du_lieu


def ghi_du_lieu(du_lieu):
    """Ghi toan bo du lieu vao data.json."""
    with DUONG_DAN_DU_LIEU.open("w", encoding="utf-8") as tep:
        json.dump(du_lieu, tep, ensure_ascii=False, indent=4)


def lay_danh_sach_nl():
    """Tra ve danh sach nguyen lieu de cac module cung su dung."""
    return doc_du_lieu()["nguyen_lieu"]


def them_nguyen_lieu_du_lieu(nguyen_lieu):
    """Them mot nguyen lieu moi va luu lai."""
    du_lieu = doc_du_lieu()
    ma = nguyen_lieu.get("ma")

    if not ma:
        raise ValueError("Nguyen lieu phai co ma.")

    if any(nl.get("ma") == ma for nl in du_lieu["nguyen_lieu"]):
        raise ValueError(f"Ma nguyen lieu {ma} da ton tai.")

    du_lieu["nguyen_lieu"].append(nguyen_lieu)
    ghi_du_lieu(du_lieu)


def cap_nhat_nguyen_lieu(ma, thong_tin_moi):
    """Cap nhat thong tin nguyen lieu theo ma."""
    du_lieu = doc_du_lieu()

    for i, nl in enumerate(du_lieu["nguyen_lieu"]):
        if nl.get("ma") == ma:
            du_lieu["nguyen_lieu"][i].update(thong_tin_moi)
            ghi_du_lieu(du_lieu)
            return True

    return False


def xoa_nguyen_lieu_du_lieu(ma):
    """Xoa nguyen lieu theo ma."""
    du_lieu = doc_du_lieu()
    danh_sach = du_lieu["nguyen_lieu"]
    moi = [nl for nl in danh_sach if nl.get("ma") != ma]

    if len(moi) == len(danh_sach):
        return False

    du_lieu["nguyen_lieu"] = moi
    ghi_du_lieu(du_lieu)
    return True


def lay_danh_sach_phieu_nhap():
    return doc_du_lieu()["phieu_nhap"]


def luu_phieu_nhap(phieu):
    du_lieu = doc_du_lieu()
    du_lieu["phieu_nhap"].append(phieu)
    ghi_du_lieu(du_lieu)


def lay_danh_sach_phieu_xuat():
    return doc_du_lieu()["phieu_xuat"]


def luu_phieu_xuat(phieu):
    du_lieu = doc_du_lieu()
    du_lieu["phieu_xuat"].append(phieu)
    ghi_du_lieu(du_lieu)

