"🔹 1️⃣ Linear Time O(n) → Preprocessing Data"

"""
Dalam ML, kita sering bersihin dan normalisasi data sebelum training.
Misalnya, kita mau menghapus missing values dari dataset besar.
"""

import pandas as pd

# Contoh dataset
data = pd.DataFrame({
    "name": ["Ami", "Budi", "Charlie", "Dina", None],
    "height": [170, 165, 180, 160, None],
    "weight": [65, 70, 80, 55, 75]
})

# Hapus baris dengan missing values (O(n))
clean_data = data.dropna()
print(clean_data)
