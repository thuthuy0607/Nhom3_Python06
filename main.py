
def main():
    while True:
        print("\n====================================")
        print(" CHUONG TRINH QUAN LY KHO NGUYEN LIEU")
        print("====================================")
        print("1. Quan ly nguyen lieu")
        print("2. Nhap kho")
        print("3. Xuat kho")
        print("4. Thong ke va canh bao")
        print("0. Thoat chuong trinh")

        chon = input("Chon chuc nang: ").strip()

        if chon == "1":
            from nguyen_lieu import menu_nguyen_lieu
            menu_nguyen_lieu()

        elif chon == "2":
            from nhap_kho import menu_nhap_kho
            menu_nhap_kho()

        elif chon == "3":
            from xuat_kho import menu_xuat_kho
            menu_xuat_kho()

        elif chon == "4":
            from thong_ke import menu_thong_ke
            menu_thong_ke()

        elif chon == "0":
            print("Cam on ban da su dung chuong trinh!")
            break

        else:
            print("Lua chon khong hop le. Vui long chon lai.")


if __name__ == "__main__":
    main()

