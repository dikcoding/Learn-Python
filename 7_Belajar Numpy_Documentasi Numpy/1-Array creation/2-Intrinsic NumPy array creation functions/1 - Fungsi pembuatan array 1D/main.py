# Fungsi pembuatan array 1D misalnya numpy.linspace dan numpy.arange umumnya memerlukan setidaknya dua masukan, (start) dan (stop)

import numpy as np

arange = np.arange(10)
print(arange)

b = np.arange(2, 10, dtype=float)
print(b)

c = np.arange(2, 3, 0.1)
print(c)

# numpy.arange adalah menggunakan nilai awal, akhir dan langkah integer.
# numpy.arange(start, stop, step) stop


# numpy.linspaceakan membuat array dengan jumlah elemen tertentu, dan diberi jarak yang sama antara nilai awal dan akhir yang ditentukan
linspace = np.linspace(1.,4.,6)
print(linspace)
