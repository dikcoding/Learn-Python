class Mahasiswa():
    def __init__(self, name, nim, umur):
        self.__name = name    #atribu private
        self.__nim = nim      #atribu private
        self.__umur = umur    #atribu private

    # Getter untuk atribut name
    def get_name(self):
        return self.__name
    
    # Setter untuk atribut name
    def set_name(self, name):
        self.__name = name

    # Getter untuk atribut nim
    def get_nim(self):
        return self.__nim

    # Setter untuk atribut nim
    def set_nim(self, nim):
        self.__nim = nim

    # Getter untuk atribut umur
    def get_umur(self):
        return self.__umur
    
    # Setter untuk atribut umur
    def set_umur(self, umur):
        self.__umur = umur

# membuat objek dari class Mahasiswa
mhw = Mahasiswa("Budi", "180411100001", 20)

# Mengakses data melalui getter
print(mhw.get_name())
print(mhw.get_nim())
print(mhw.get_umur())

# Mengakses data melalui setter
mhw.set_name("Andi")
mhw.set_umur(21)

# Mengakses data yang telah diubah melalui setter
print(mhw.get_name())
print(mhw.get_umur())
