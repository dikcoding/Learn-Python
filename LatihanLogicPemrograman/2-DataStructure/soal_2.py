from collections import defaultdict, deque

film = [
    {'judul': 'Avengers: Endgame', 'genre': 'Superhero', 'rating': 8.4, 'tahun': 2019},
    {'judul': 'Spider-Man: No Way Home', 'genre': 'Superhero', 'rating': 8.3, 'tahun': 2021},
    {'judul': 'The Shawshank Redemption', 'genre': 'Drama', 'rating': 9.3, 'tahun': 1994},
    {'judul': 'The Godfather', 'genre': 'Crime', 'rating': 9.2, 'tahun': 1972},
    {'judul': 'The Dark Knight', 'genre': 'Superhero', 'rating': 9.0, 'tahun': 2008}
]

# mengelompokkan film berdasarkan genre
genre_dict = defaultdict(list)
for f in film:
    genre_dict[f['genre']].append(f)

# menghitung rata-rata rating untuk setiap genre
avg_rating = {genre: sum(f['rating'] for f in films) / len(films) for genre, films in genre_dict.items()}

# menampilkan genre dengan rata-rata paling tertinggi
highest_rated_genre = max(avg_rating, key=(avg_rating.get))

# menampilkan daftar film yang di rilis setelah tahun 2000
filter_after = [f['judul'] for f in film if f['tahun'] > 2000]

# Tantangan tambahan
# Dictionery comprehension untuk genre sebagai key dan list film sebagai value (terurut berdasarkan rating)
genre_sorted = {genre: sorted(films, key=lambda x: x['rating'], reverse=True) for genre, films in genre_dict.items()}

# menggunakan deque sebagai stack untuk traversal daftar film
stack = deque(film)
print("\nFilm dalam stack :")
while stack:
    print(stack.pop())

# menggunakan deque sebagai queue untuk traversal daftar film
queue = deque(film)
print("\nFilm dalam queue : ")
while queue:
    print(queue.popleft())

# menggunakan generator expression untuk mendapatkan semua judul film
def film_titles():
    return(f['judul'] for f in film)

print("\njudul Film : ")
for title in film_titles():
    print(title)

# Output hasil
print("\nGenre dengan rating tertinggi : ", highest_rated_genre)
print("-----------------------------------")
print("Film di rilis setelah tahun 2000 : ", filter_after)
print("-----------------------------------")
print("Rata-rata rating per genre : ", avg_rating)
print("-----------------------------------")
print("Film berdasarkan genre (diurutkan) : ", genre_sorted)