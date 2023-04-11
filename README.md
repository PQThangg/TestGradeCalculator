# **ASSIGNMENT 01**
## **Tên dự án: Tính toán và phân tích điểm thi (Test Grade Calculator)**
Đây là một chương trình để tính toán điểm thi cho nhiều lớp với sĩ số hàng nghìn học sinh. Mục đích của chương trình giúp giảm thời gian chấm điểm. Các chương trình với các tác vụ sau: 

- Mở các tập tin văn bản bên ngoài được yêu cầu với exception-handling
- Quét từng dòng của câu trả lời bài thi để tìm dữ liệu hợp lệ và cung cấp báo cáo tương ứng
- Chấm điểm từng bài thi dựa trên tiêu chí đánh giá (rubric) được cung cấp và báo cáo
- Tạo tập tin kết quả được đặt tên thích hợp
## **Hướng dẫn chạy dự án**
*Task1*
```
try:
    b = input("Nhap ten file can doc (nhap class1.txt cho file class1) = ")
    a = open(b)
    print('In file thanh cong:',b)
except:
    print('khong the tim thay file')
```
Nhập tên file theo như yêu cầu, đảm bảo tệp mã nguồn nằm trong cùng thư mục với tệp dữ liệu được nhập.

Có thể tải tất cả các file từ class1 đến class8 lên jupyter Notebook, sau đó chạy chương trình.

*Task2*
```
try:
    b = input("Nhap ten file can doc (nhap class1.txt cho file class1) = ")
    a = open(b)
    print('In file thanh cong:',b)
except:
    print('khong the tim thay file')
```
Nhập lại tên file để làm việc trong task mới. Nhập đúng tên file chương trình sẽ trả về báo dữ liệu trong tệp có đúng định dạng chưa, nhập sai tên file chương trình sẽ dừng.

*Task3*
```
try:
    b = input("Nhap ten file can doc (nhap class1.txt cho file class1) = ")
    a = open(b)
    print('In file thanh cong:',b)
except:
    print('khong the tim thay file')
```
Tương tự task 2. Nhập đúng sẽ trả về điểm thi của lớp được nhập bao gồm:

1. Số lượng học sinh đạt điểm cao (>80).

2. Điểm trung bình.

3. Điểm cao nhất.

4. Điểm thấp nhất.

5. Miền giá trị của điểm (cao nhất trừ thấp nhất).

6. Giá trị trung vị .

7. Các câu hỏi bị học sinh bỏ qua nhiều nhất theo thứ tự: số thứ tự câu hỏi - số lượng học sinh bỏ qua -  tỉ lệ bị bỏ qua (nếu có cùng số lượng cho nhiều câu hỏi bị bỏ thì phải liệt kê ra đầy đủ).

8. Câu hỏi bị học sinh làm sai nhiều nhất theo thứ tự số thứ tự: số thứ tự câu hỏi - số lượng học sinh trả lời sai - tỉ lệ bị sai (nếu có cùng số lượng cho nhiều câu hỏi bị sai thì phải liệt kê ra đầy đủ).

Nhập sai tên file dừng chương trình.

*Task4*
```
try:
    b = input("Nhap ten lop can tao tep diem (nhap class1.txt cho file class1) = ")
    a = open(b)
except:
    print('khong the tim thay file')
```
Tiếp tục nhập tên file để tạo file kết quả.
```
d = input("Dat ten file cua lop can tao tep diem (nhap class1_diem.txt cho file class1) = ")
c = open(d,'w')
```
Nhập tên file kết quả cho file dữ liệu vừa nhập ở trên, (nên đặt tên tệp này dựa trên tên tệp gốc được cung cấp — ví dụ: nếu muốn phân tích “class1.txt”, nên đặt tên là “class1_diem.txt”), sau đó chương trình sẽ trả về file điểm.

Hoàn thành chương trình với 4 task.
# ĐẾN ĐÂY LÀ KẾT THÚC RỒI.
*Thank you!*