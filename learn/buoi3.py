class sinhvien:
	def __init__(self,ten, namsinh, gioitinh):  #hàm khởi tạo, thuộc tính
		self.hoten= ten
		self.nam = namsinh
		self.gt = gioitinh
	def xuat(self):
		print("ho va ten: ",self.hoten)
		print("nam sinh: ",self.nam)
		print("gioi tinh la: ",self.gt)
sinhvien1= sinhvien("tran duc bo",2003,"nu")
sinhvien1.xuat()
sinhvien2 = sinhvien("nguyen gia truong",2001,"bede")
sinhvien2.xuat()