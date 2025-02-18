# List comprehesion (Menggunakan Lebih banyak memori)
square_list = [x**2 for x in range(10)]
print(square_list)

print("-------------------")

# Generator Expression (Lebih hemat memerori)
square_generator = (x**2 for x in range(10))
print(square_generator)
print(list(square_generator))
# Generator dengan fungsi yang menerima Iterator: seperti sum(), max(), min(), dan any()

# menggunakan sum()
print("-------------------")
total = (x**2 for x in range(1, 11))
print (total)
print (list(total))

# menggunakan any() atau all()
print("-------------------")
number = [2, 4, 6, 8, 9]
is_all_even = all(x % 2 == 0 for x in number)
is_any_odd = any(x % 2 !=  0 for x in number) 

print(is_all_even)
print(is_any_odd)