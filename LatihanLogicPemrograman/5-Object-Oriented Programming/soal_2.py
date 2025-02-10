

class Pelanggan:
    def __init__(self, id_pelanggan, name, usia, jenis_kelamin, riwayat_pembelian, tingkat_kepuasan):
        self.id_pelanggan = id_pelanggan
        self.name = name
        self.usia = usia
        self.jenis_kelamin = jenis_kelamin
        self.riwayat_pembelian = riwayat_pembelian
        self.tingkat_kepuasan = tingkat_kepuasan
    
    @property
    def tingkat_kepuasan(self):
        return self._tingkat_kepuasan
    
    @tingkat_kepuasan.setter
    def tingkat_kepuasan(self, nilai):
        if 1 <= nilai <= 5:
            self._tingkat_kepuasan = nilai
        else:
            raise ValueError("Tingkat kepuasan harus dalam rentang 1-5")
    
    def tampilakan_info(self):
        info = f"ID pelanggan: {self.id_pelanggan}\nNama: {self.nama}\nUsia: {self.usia}\n"
        print(info)