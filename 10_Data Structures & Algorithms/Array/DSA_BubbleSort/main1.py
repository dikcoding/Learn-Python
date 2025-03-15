"Peningkatan Sortiran Gelembung"

"Bayangkan array tersebut hampir terurut, dengan angka terendah di awal, seperti contoh berikut:"

my_array = [7, 3, 9, 12, 11]

n = len(my_array)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            swapped = True
        if not swapped:
            break
print("Sorted Array:", my_array)