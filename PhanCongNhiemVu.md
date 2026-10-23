
# PHÂN CÔNG NHIỆM VỤ
## Đề tài: Ứng dụng quản lý kho nguyên liệu quán ăn

### 1. Mục tiêu dự án
Xây dựng chương trình Python hỗ trợ quán ăn quản lý nguyên liệu, nhập kho, xuất kho, thống kê tồn kho, cảnh báo nguyên liệu sắp hết, theo dõi hạn sử dụng và lưu trữ dữ liệu.

### 2. Phân công thành viên

#### Thành viên 1: Nguyễn Rah Lan Tuyết Trâm 
**File phụ trách:** `nguyen_lieu.py`

**Nhiệm vụ:**
- Thiết kế cấu trúc dữ liệu nguyên liệu.
- Xây dựng chức năng thêm nguyên liệu.
- Xây dựng chức năng hiển thị danh sách nguyên liệu.
- Xây dựng chức năng tìm kiếm nguyên liệu.
- Xây dựng chức năng sửa thông tin nguyên liệu.
- Xây dựng chức năng xóa nguyên liệu.
- Kiểm tra mã nguyên liệu trùng lặp, tên rỗng, số lượng và đơn giá không âm.
- Viết phần báo cáo về chức năng quản lý nguyên liệu.

#### Thành viên 2: Trương Như Phúc
**File phụ trách:** `nhap_kho.py`

**Nhiệm vụ:**
- Xây dựng chức năng tạo phiếu nhập kho.
- Thêm chi tiết nhập kho.
- Kiểm tra mã nguyên liệu tồn tại.
- Kiểm tra số lượng và đơn giá nhập lớn hơn 0.
- Tính thành tiền nhập kho.
- Cập nhật số lượng tồn kho sau khi nhập.
- Hiển thị phiếu nhập kho.
- Viết phần báo cáo về quy trình nhập kho.

#### Thành viên 3: Trương Hồng Phúc
**File phụ trách:** `xuat_kho.py`

**Nhiệm vụ:**
- Xây dựng chức năng tạo phiếu xuất kho.
- Kiểm tra số lượng nguyên liệu trước khi xuất.
- Thêm chi tiết xuất kho.
- Không cho phép xuất vượt quá số lượng tồn.
- Cập nhật số lượng tồn kho sau khi xuất.
- Hiển thị phiếu xuất kho.
- Viết phần báo cáo về quy trình xuất kho.

#### Thành viên 4: Tiêu Thị Thu Thủy
**File phụ trách:** `thong_ke.py`

**Nhiệm vụ:**
- Thống kê tổng số nguyên liệu.
- Thống kê nguyên liệu còn hàng và nguyên liệu sắp hết.
- Tính tổng giá trị tồn kho.
- Cảnh báo nguyên liệu sắp hết theo ngưỡng thống nhất của nhóm.
- Kiểm tra nguyên liệu sắp hết hạn hoặc đã hết hạn.
- Hiển thị báo cáo thống kê kho.
- Viết phần báo cáo về chức năng thống kê và cảnh báo.

### 3. Nhiệm vụ chung của cả nhóm
- Thống nhất cấu trúc dữ liệu, tên biến, tên hàm và cách lưu dữ liệu.
- Cùng xây dựng và tích hợp chương trình trong `main.py`.
- Phối hợp xây dựng `du_lieu.py` để đọc và ghi dữ liệu.
- Sử dụng `data.json` để lưu dữ liệu nếu cả nhóm thống nhất dùng định dạng JSON.
- Kiểm thử các chức năng và xử lý lỗi.
- Kiểm tra khả năng chạy của chương trình sau khi tích hợp.
- Mỗi thành viên commit và push các file do mình phụ trách lên GitHub.
- Cùng rà soát và hoàn thiện sản phẩm trước khi nộp.

### 4. Quy ước chung
- Mã nguyên liệu sử dụng tên biến `ma`.
- Tên nguyên liệu sử dụng tên biến `ten`.
- Đơn vị tính sử dụng tên biến `don_vi`.
- Số lượng tồn sử dụng tên biến `so_luong`.
- Đơn giá sử dụng tên biến `don_gia`.
- Tên hàm thêm bắt đầu bằng `them_`.
- Tên hàm sửa bắt đầu bằng `sua_`.
- Tên hàm xóa bắt đầu bằng `xoa_`.
- Tên hàm hiển thị bắt đầu bằng `hien_thi_`.
- Không tự ý thay đổi tên hàm hoặc cấu trúc dữ liệu đã thống nhất nếu chưa trao đổi với nhóm.

