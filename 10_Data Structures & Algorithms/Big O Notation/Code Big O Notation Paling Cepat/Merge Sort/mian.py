import pandas as pd

# Dataset awal
data = pd.DataFrame({
    "name": ["Ami", "Budi", "Charlie", "Dina", "Eko"],
    "height": [170, 165, 180, 160, 175],
    "weight": [65, 70, 80, 55, 75]
})

print("Sebelum Sorting:")
print(data)

# Fungsi Merge Sort untuk sorting berdasarkan tinggi badan (height)
def merge_sort_dataframe(df):
    if len(df) <= 1:
        return df
    
    mid = len(df) // 2
    left = merge_sort_dataframe(df.iloc[:mid])
    right = merge_sort_dataframe(df.iloc[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left.iloc[i]["height"] < right.iloc[j]["height"]:
            sorted_list.append(left.iloc[i])
            i += 1
        else:
            sorted_list.append(right.iloc[j])
            j += 1
    
    while i < len(left):
        sorted_list.append(left.iloc[i])
        i += 1
    while j < len(right):
        sorted_list.append(right.iloc[j])
        j += 1

    return pd.DataFrame(sorted_list)

# Sorting dataset berdasarkan tinggi badan (height)
sorted_data = merge_sort_dataframe(data)
print("\nSetelah Sorting dengan Merge Sort:")
print(sorted_data)
