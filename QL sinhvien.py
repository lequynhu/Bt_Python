class Sinhvien:

    def __init__(self, Masv, Tensv, Ngaysinh, Lop, DiemTichLuy, Sodt):
        self.Masv = Masv
        self.Tensv = Tensv
        self.Ngaysinh = Ngaysinh
        self.Lop = Lop
        self.DiemTichLuy = float(DiemTichLuy)
        self.Sodt = Sodt

    def InThongTinSV(self):
        print('Mã SV           :', self.Masv)
        print('Tên SV          :', self.Tensv)
        print('Ngày Sinh       :', self.Ngaysinh)
        print('Lớp             :', self.Lop)
        print('Điểm tích lũy   :', self.DiemTichLuy)
        print('Số điện thoại ', self.Sodt)

    def XepLoai(self):
        if self.DiemTichLuy >= 3.5:
            print('Xuất sắc')
        elif 3.2 <= self.DiemTichLuy < 3.5:
            print('Giỏi')
        elif 2.5 <= self.DiemTichLuy < 3.2:
            print('Khá')
        elif 2 <= self.DiemTichLuy < 2.5:
            print('Trung bình')
        else:
            print('Kém')

    def SuaThongTinSV(self):
        sdtm = int(input("Số điện thoại mới: "))
        self.Sodt = sdtm
        print("Cập nhật thành công!")

s1=Sinhvien('201112345','Nguyễn Tiến Thành','12/10/2002','45k14','3.9','')
s2=Sinhvien('201112346','Phùng Lê Na','05/06/2001','45k14','1.9','')
s3=Sinhvien('201112347','Trần Văn Hùng','07/11/2002','45k21.1','2.3','')

#Sử dụng phương thức XepLoai để kiểm tra xếp loại học lực của sinh viên Nguyễn Tiến Thành
s1.XepLoai()

#Sử dụng phương thức SuaThongTinSV để đổi số điện thoại của Phùng Lê Na thành 091234567
s2.SuaThongTinSV()

#In thông tin của 3 sinh viên ra màn hình
s1.InThongTinSV()
s2.InThongTinSV()
s3.InThongTinSV()















