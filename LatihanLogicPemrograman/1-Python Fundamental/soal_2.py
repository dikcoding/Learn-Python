def costumer_kategori (jumlah_kunjungan):
    if jumlah_kunjungan < 10:
        return "Rere Visitor"
    elif 10 <= jumlah_kunjungan < 50:
        return "Occasional Visitor"
    else:
        return "Frequen Visitor"

costumers = [
    {"id": 10, "jumlah_kunjungan": 10,}
]

for costumer in costumers:
    costumer['kategori'] = costumer_kategori(costumer['jumlah_kunjungan'])

for costumer in costumers:
    print(f"ID Pelanggan : {costumer['id']}, Jumlah Kunjungan: {costumer['jumlah_kunjungan']}, Kategori : {costumer['kategori']}")