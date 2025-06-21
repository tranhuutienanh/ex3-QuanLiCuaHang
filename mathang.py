class MatHang:
    def __init__(self, ten, so_luong, gia, ma_vach):
        self.ten = ten
        self._so_luong = so_luong
        self.__gia = gia
        self.__ma_vach = ma_vach
    def hienthongtin(self):
        print(f'Tên mặt hàng {self.ten}')
        print(f'Số lượng mặt hàng {self._so_luong}')
        print(f'Giá của mặt hàng {self.__gia}')
        print(f'Mã vạch của sản phẩm {self.__ma_vach}')
    def hiensoluong(self):
        print(f"Số lượng còn lại {self._so_luong}")
    def lay_gia(self):
        return int(self.__gia)
    def cap_nhat_gia(self, gia_moi):
        if gia_moi <= 0:
            print("Mức gía không hợp lệ")
        else:
            self.__gia = gia_moi  
            print(f"Giá mới {gia_moi}")  
    def kiem_tra_kho(self):
        if self._so_luong >= 100:
            return("Hàng nhiều")
        elif self._so_luong <= 99 and self._so_luong >= 30:
            return("Hàng ổn định")
        else: 
            return("Sắp hết hàng")
    def cap_nhat_ma(self):
            return int(self.__ma_vach)
    def cap_nhat_ma_vach(self, ma_moi):
        ma_moi = str(ma_moi)
        if ma_moi.isdigit() and 8 <= len(ma_moi) <= 12:
            self.__ma_vach = int(ma_moi)
            print(f"Mã vạch mới: {self.__ma_vach}")
            return True
        else:
            print("Mã vạch không hợp lệ. Phải là số có từ 8 đến 12 chữ số.")
            return False

    def __str__(self):
        return(f"Mặt hàng: Tên: {self.ten}, Số lượng: {self._so_luong}, Giá: {self.__gia}")
    def ban_so_luong(self, so_luong_ban):
        if so_luong_ban <= self._so_luong:
            self._so_luong -= so_luong_ban
            print("Bạn đã bán thành công")
        else:
            print("bạn ko có đủ hàng")


ga = MatHang("gà", 50, 100, 12345678)
ga.hienthongtin()
ga.hiensoluong()
ga.lay_gia()
ga.cap_nhat_gia(150)
ga.kiem_tra_kho()
ga.cap_nhat_ma()
ga.cap_nhat_ma_vach("67890123")
ga.__str__()
ga.ban_so_luong(25)


