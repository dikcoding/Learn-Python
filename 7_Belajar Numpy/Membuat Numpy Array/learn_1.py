import numpy as np

# Membuat vector 
a = np.array([1, 2, 3, 4])
print(a)
print("-----------------------------------------")

# Membuat vector dengan range
b = np.arange(1, 10, 2) # dari (1) sampai (10), terus yang (2) ini, dia loncat contohnya dari 1 ke 3
print(b)
print("-----------------------------------------")

# Membuat linspace
c = np.linspace(1,10,4) # Jadi kalau (4) ini, kita nampilin 4 angka dari (1) sampai (10)
print(c)
print("-----------------------------------------")

# Array multidimensi / matrix
d = np.array([(1, 2, 3), (4, 5, 6)])
print(d)
print(d + 1) # Nah biasanya kalau matriks ditambah sklar, maka semua kompenennya ditambah 1
print("-----------------------------------------")

# Matriks dengan nilai nol
e = np.zeros((5,5)) # Nah kita coba pake nilai vector (5), kalau (5,5) itu di kali 5 dia
print(e)
print("-----------------------------------------")

# Matriks dengan nilai satu
f = np.ones((5,5)) # ini juga sama seperi zeros
print(f)
print("-----------------------------------------")

# Matriks Identitas
g = np.identity(5)
h = np.eye(5)
print(g)
print(h)