def them_nguyen_lieu(danh_sach):
    print("THÊM NGUYÊN LIỆU")
    
    #Nhập mã nguyên liệu
    ma = input("Mã nguyên liệu: ").strip()
    
    # Kiểm tra mã
    for nguyen_lieu in danh_sach:
        if nguyen_lieu["ma"] == ma:
            print("Mã nguyên liệu đã tồn tại!")
            return
        
    #Nhập tên
    ten = input("Tên nguyên liệu: ").strip()
    
    #Kiểm tra tên
    if ten == "":
        print("Tên nguyên liệu không được để trống!")
        return
    
    #Nhập loại nguyên liệu
    loai = input("Loại nguyên liệu: ").strip()

    #Nhập đơn vị
    don_vi = input("Đơn vị tính: ").strip()

    #Nhập số lượng
    try:
        so_luong = float(input("Số lượng: "))
        
        if so_luong < 0:
            print("Số lượng không được âm!")
            return
        
    except ValueError:
        print("Số lượng không phải là số!")
        return
    #Nhập đơn giá
    try:
        don_gia = float(input("Đơn giá: "))
        
        if don_gia < 0:
            print("Đơn giá không được âm!")
            return
        
    except ValueError:
        print("Đơn giá phải là số!")
        return
    
    #Nhập hạn sử dụng
    han_su_dung = input("Hạn sử dụng (dd/mm/yyyy): ").strip()
    
    #Thông tin nguyen liệu
    nguyen_lieu_moi = {
        "ma": ma,
        "ten": ten,
        "loai": loai,
        "don_vi": don_vi,
        "so_luong": so_luong,
        "don_gia": don_gia,
        "han_su_dung": han_su_dung
    }
    
    #Thêm vào danh sách
    danh_sach.append(nguyen_lieu_moi)
    print("Thêm nguyên liệu thành công!")
    
def hien_thi_danh_sach(danh_sach):
    print("DANH SÁCH NGUYÊN LIỆU")
    
    if len(danh_sach) == 0:
        print("Danh sách nguyên liệu đang trống!")
        return
    for nguyen_lieu in danh_sach:
        print("Mã:", nguyen_lieu["ma"])
        print("Tên:", nguyen_lieu["ten"])
        print("Loại:", nguyen_lieu["loai"])
        print("Đơn vị:", nguyen_lieu["don_vi"])
        print("Số lượng:", nguyen_lieu["so_luong"])
        print("Đơn giá:", nguyen_lieu["don_gia"])
        print("Hạn sử dụng:", nguyen_lieu["han_su_dung"])
    
def tim_nguyen_lieu(danh_sach):
    print("TÌM KIẾM NGUYÊN LIỆU")
    
    tu_khoa = input("Nhập mã hoặc tên nguyên liệu cần tìm: ").strip().lower()
    
    tim_thay = False
    
    for nguyen_lieu in danh_sach:
        if (tu_khoa in nguyen_lieu["ma"].lower()
                or tu_khoa in nguyen_lieu["ten"].lower()):           
            print("Mã:", nguyen_lieu["ma"])
            print("Tên:", nguyen_lieu["ten"])
            print("Loại:", nguyen_lieu["loai"])
            print("Đơn vị:", nguyen_lieu["don_vi"])
            print("Số lượng:", nguyen_lieu["so_luong"])
            print("Đơn giá:", nguyen_lieu["don_gia"])
            print("Hạn sử dụng:", nguyen_lieu["han_su_dung"])
            
            tim_thay = True
            
    if not tim_thay:
        print("Không tìm thấy nguyên liệu")
        
def sua_nguyen_lieu(danh_sach):
    print("SỬA NGUYÊN LIỆU")
    
    ma = input("Nhập mã nguyên liệu cần sử: ").strip()
    
    for nguyen_lieu in danh_sach:
        if nguyen_lieu["ma"] ==  ma:
             print("Đã tìm thấy: ",nguyen_lieu["ten"])
       
        ten = input("Tên mới: ").strip()
        if ten == "":
            print("Tên không được để trống!")
            return
        loai = input("Loại mớii: ").strip()
        don_vi = input("Đơn vị mới: ").strip()
        
        try:
            so_luong = float(input("Số lượng mớii: "))
            
            if so_luong < 0:
                print("Số lượng không được âm!")
                return
            
        except ValueError:
            print("Số lượng phải là số!")
            return
        
        try:
            don_gia = float(input("Đơn giá mới: "))
            if don_gia < 0:
                print("Đơn giá không được âm!")
                return
            
        except ValueError:
            print("Đơn giá phải là số!")
            return
        
        han_su_dung =  input("Hạn sử dụng mới: ").strip()
        
        #Cập nhật thông tin
        nguyen_lieu["ten"] = ten
        nguyen_lieu["loai"] = loai
        nguyen_lieu["don_vi"] = don_vi
        nguyen_lieu["so_luong"] = so_luong
        nguyen_lieu["don_gia"] = don_gia
        nguyen_lieu["han_su_dung"] = han_su_dung
        
        print("Sử nguyên liệu thành công!")
        return
    print("Không tìm thấy nguyên liệu!")
    
def xoa_nguyen_lieu(danh_sach):
    print("XÓA NGUYÊN LIỆU")
    
    ma = input("Nhập mã nguyên liệu cần xóa: ").strip()
    
    for i in range(len(danh_sach)):
         if danh_sach[i]["ma"] == ma:
             print("Nguyên liệu:", danh_sach[i]["ten"])
             
             xac_nhan = input("Bạn có chắc muốn xóa? (y/n): ").lower()
             
             if xac_nhan == "y":
                 danh_sach.pop(i)
                 print("Xóa nguyên liệu thành công!")
             else:
                print("Đã hủy xóa.")                
             return
        
    print("Không tìm thấy mã nguyên liệu!")

def menu_nguyen_lieu(danh_sach):
    while True:
        print("QUẢN LÝ NGUYÊN LIỆU")
        print("1. Thêm nguyên liệu")
        print("2. Hiển thị nguyên liệu")
        print("3. Tìm kiếm")
        print("4. Sửa nguyên liệu")
        print("5. Xóa nguyên liệu")
        print("0. Quay lại")

        lua_chon = input("Chọn: ")

        if lua_chon == "1":
            them_nguyen_lieu(danh_sach)

        elif lua_chon == "2":
            hien_thi_danh_sach(danh_sach)

        elif lua_chon == "3":
            tim_nguyen_lieu(danh_sach)

        elif lua_chon == "4":
            sua_nguyen_lieu(danh_sach)

        elif lua_chon == "5":
            xoa_nguyen_lieu(danh_sach)

        elif lua_chon == "0":
            print("Đã thoát quản lý nguyên liệu.")
            break

        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__": 
    danh_sach = [] 
    menu_nguyen_lieu(danh_sach)
