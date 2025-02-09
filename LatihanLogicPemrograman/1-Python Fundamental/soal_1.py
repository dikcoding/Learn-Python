# Fungsi untuk mengategorikan pelanggan berdasarkan total pembelian
def categorize_costumer(total_pembelian):
    if total_pembelian < 1000000:
        return "Low Spender"
    elif 1000000 <= total_pembelian < 5000000:
        return "Medium Spender"
    else:
        return "High Spender"


# Data Pelanggan (misal dalam bantuk List of dictionaries)
customers = [
    {"id": 1, "total_pembelian": 800000},
    {"id": 2, "total_pembelian": 2500000},
    {"id": 3, "total_pembelian": 6000000},
    {"id": 4, "total_pembelian": 1500000},
    {"id": 5, "total_pembelian": 100000}
]

# Menggunakan loop untuk mengkategorikan setiap pelanggan
for costumer in customers:
    costumer['kategori'] = categorize_costumer(costumer['total_pembelian'])

for customer in customers:
    print(f"ID Pelanggan: {customer['id']}, Total Pembelian: {customer['total_pembelian']}, Kategori: {customer['kategori']}")