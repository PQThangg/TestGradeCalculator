#!/usr/bin/env python
# coding: utf-8

# # Task1

# In[1]:


#Task1:
try:
    b = input("Nhap ten file can doc (nhap class1.txt cho file class1) = ")
    a = open(b)
    print('In file thanh cong:',b)
except:
    print('khong the tim thay file')


# # Task2

# In[2]:


#Task2:
# Mở file cần phân tích
try:
    b = input("Nhap ten file can doc (nhap class1.txt cho file class1) = ")
    a = open(b)
    print('In file thanh cong:',b)
except:
    print('khong the tim thay file')

    
print('**** ANALYZING ****')

# Tính tổng số dòng của file
with open(b) as f:
    text = f.readlines()
    size = len(text)

f1 = open(b)

# Vòng lặp xét dòng dữ liệu hợp lệ hay không hợp lệ
Loi = 0
Sodong = 1
while Sodong <= size: 
    k = f1.readline()
    if len(k.split(',')) != 26:
        print('Dong du lieu khong hop le: khong chua danh sach 26 gia tri duoc phan tach bang dau phay')
        print(k)
        Loi +=1
    else:
        if len(k.split(',')[0]) != 9 or k.split(',')[0][0]!='N' or k.split(',')[0][1:9].isdecimal() is False:
            print('Dong du lieu khong hop le: Dinh dang N# khong hop le')
            print(k)
            Loi +=1
    Sodong +=1

if Loi == 0:
    print('khong tim thay loi')

print('**** REPORT ****')
print('Tong so dong cua du lieu:',size)
print('Tong so dong loi cua du lieu:',Loi)


# # Task3

# In[2]:


#Task3:
import collections

# Mở file cần phân tích
try:
    b = input("Nhap ten file can doc (nhap class1.txt cho file class1) = ")
    a = open(b)
    print('In file thanh cong:',b)
except:
    print('khong the tim thay file')

    
print('**** ANALYZING ****')

# Tính tổng số dòng của file
with open(b) as f:
    text = f.readlines()
    size = len(text)

f1 = open(b)

# Vòng lặp xét dòng dữ liệu hợp lệ hay không hợp lệ
Loi = 0
Sodong = 1
while Sodong <= size:
    k = f1.readline()
    if len(k.split(',')) != 26:
        print('Dong du lieu khong hop le: khong chua danh sach 26 gia tri duoc phan tach bang dau phay')
        print(k)
        Loi +=1
    else:
        if len(k.split(',')[0]) != 9 or k.split(',')[0][0]!='N' or k.split(',')[0][1:9].isdecimal() is False:
            print('Dong du lieu khong hop le: Dinh dang N# khong hop le')
            print(k)
            Loi +=1
    Sodong +=1

if Loi == 0:
    print('khong tim thay loi')

print('**** REPORT ****')
print('Tong so dong cua du lieu:',size)
print('Tong so dong loi cua du lieu:',Loi)

# Vòng lặp xét đáp án của file dữ liệu so với đáp án mẫu
f2=open(b)
Dap_an = ['B','A','D','D','C','B','D','A','C','C','D','B','A','B','A','C','B','D','A','C','A','A','B','D','D']
Sodong=1
Diem_cao=0
Tong_diem=0
Diem_cao_nhat=0
Diem_thap_nhat=100
List_diem = []
List_boqua = []
List_sai = []

while Sodong<=size:
    k1 = f2.readline() 
    i=0
    dung=0
    sai=0
    boqua=0
    # Xét dòng dữ liệu hợp lệ mới tính điểm
    if len(k1.split(','))==26 and len(k1.split(',')[0])==9 and k1.split(',')[0].startswith('N') and k1.split(',')[0][1:9].isdecimal() is True:
        while i<25:
            if i<24:
                if k1.split(',')[i+1] == '':
                    boqua+=1
                    List_boqua.append(i+1)
                else:
                    if k1.split(',')[i+1] == Dap_an[i]:
                        dung+=1
                    else:
                        sai+=1
                        List_sai.append(i+1)
            # Vì đáp án cuối có thêm ký tự xuống dòng nên xét riêng
            else:
                if k1.split(',')[25] == '\n':
                    boqua+=1
                    List_boqua.append(i+1)
                else:
                    if k1.split(',')[25] == Dap_an[24]:
                        dung+=1
                    else:
                        sai+=1
                        List_sai.append(i+1)
            i+=1
    # Tính điểm cho từng dòng dữ liệu và đưa điểm số vào List điểm
    Diem_so=dung*4 - sai
    List_diem.append(Diem_so)
    Sodong+=1
# Những dòng dữ liệu không hợp lệ sẽ được ghi 0 điểm vào list, xóa những điểm 0 này ra khỏi List điểm
Xoa_0 = [num for num in List_diem if num *2 != 0]
Diem_sx = sorted(Xoa_0)
# Xét những điểm số >80 là đạt điểm cao
for j in Diem_sx:
    if j > 80:
        Diem_cao+=1
        
# In ra các báo cáo về điểm số
print('Tong so hoc sinh dat diem cao:',Diem_cao)
print('Diem trung binh:',round(sum(Diem_sx)/(size-Loi),2))
print('Diem cao nhat:',Diem_sx[-1])
print('Diem thap nhat:',Diem_sx[0])
print('Mien gia tri cua diem:',Diem_sx[-1]-Diem_sx[0])

# Tìm giá trị trung vị
if (size-Loi)%2!=0:
    print('Gia tri trung vi:',Diem_sx[int((size-Loi)/2)])
else:
    print('Gia tri trung vi:',round((Diem_sx[int((size-Loi)/2-1)]+Diem_sx[int((size-Loi)/2)])/2,2))

# Xác định những câu hỏi học sinh bỏ qua nhiều nhất
Boqua_sx = sorted(List_boqua)
Boqua_nhieu = collections.Counter(Boqua_sx)
Soluong_boqua = []
print('Cau hoi hoc sinh bo qua nhieu nhat:')
for s in Boqua_nhieu:
    Soluong_boqua.append(Boqua_nhieu[s])
for l in Boqua_nhieu:
    if Boqua_nhieu[l]==max(Soluong_boqua):
        print(l,'-',max(Soluong_boqua),'-',round(max(Soluong_boqua)/(size-Loi),2))
        
# Xác định câu hỏi học sinh làm sai nhiều nhất        
Sai_sx = sorted(List_sai)
Sai_nhieu = collections.Counter(Sai_sx)
Soluong_sai = []
print('Cau hoi hoc sinh lam sai nhieu nhat:')
for s1 in Sai_nhieu:
    Soluong_sai.append(Sai_nhieu[s1])
for l1 in Sai_nhieu:
    if Sai_nhieu[l1]==max(Soluong_sai):
        print(l1,'-',max(Soluong_sai),'-',round(max(Soluong_sai)/(size-Loi),2))


# # Task4

# In[4]:


#Task4:
# Mở file cần tạo file kết quả
try:
    b = input("Nhap ten lop can tao tep diem (nhap class1.txt cho file class1) = ")
    a = open(b)
except:
    print('khong the tim thay file')

# Tính tổng số dòng dữ liệu    
with open(b) as f:
    text = f.readlines()
    size = len(text)

# Đặt tên file kết quả - mở file, file chưa có sẽ được tạo mới   
d = input("Dat ten file cua lop can tao tep diem (nhap class1_diem.txt cho file class1) = ")
c = open(d,'w')
   
# Vòng lặp ghi điểm vào file vừa mở
f3=open(b)
Dap_an = ['B','A','D','D','C','B','D','A','C','C','D','B','A','B','A','C','B','D','A','C','A','A','B','D','D']
Sodong=1
while Sodong<=size:
    k2 = f3.readline() 
    i=0
    dung=0
    sai=0
    boqua=0
    if len(k2.split(','))==26 and len(k2.split(',')[0])==9 and k2.split(',')[0].startswith('N') and k2.split(',')[0][1:9].isdecimal() is True:
        while i<25:
            if i<24:
                if k2.split(',')[i+1] == '':
                    boqua+=1
                    List_boqua.append(i+1)
                else:
                    if k2.split(',')[i+1] == Dap_an[i]:
                        dung+=1
                    else:
                        sai+=1
                        List_sai.append(i+1)
            else:
                if k2.split(',')[25] == '\n':
                    boqua+=1
                    List_boqua.append(i+1)
                else:
                    if k2.split(',')[25] == Dap_an[24]:
                        dung+=1
                    else:
                        sai+=1
                        List_sai.append(i+1)
            i+=1
    Diem_so=dung*4 - sai
    List_diem.append(Diem_so)
    if Diem_so !=0:
        c.write(str(k2[:9])+', ')
        c.write(str(Diem_so)+"\n")
    Sodong+=1
print('File',d,'da duoc tao thanh cong')


# In[5]:


#Task4:
# Mở file điểm
try:
    d = input("Nhap ten file cua lop can xem diem (nhap class1_diem.txt cho file class1) = ")
    c = open(d)
    print('In file thanh cong:',d)
    print(c.read())
except:
    print('khong the tim thay file')


# In[ ]:





# In[ ]:




