Hoten =  input('Ho ten: ')
songay = int(input('So ngay cong: '))
dongia = int(input('Don gia ngay cong: '))
phucap = float(input('He so phu cap: '))
tamung = int(input('Tam ung: '))
luong = dongia * songay * phucap
thuclinh= luong - tamung
print("Nhan vien",Hoten,end=", ")
print("Co tien Luong=",(round(luong,1)),end=", ",sep="")
print("Tam ung=",tamung,end="",sep="")
print(" va Thuc linh=",(round(thuclinh,1)),sep="")

