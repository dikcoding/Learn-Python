import json

# Membaca file JSON
with open('6_Python Standard Library/Working with CSV and JSON files/JSON/test.json') as jsonfile:
    data = json.load(jsonfile)
    print(data)


# Menulis ke FIle JSON

data = {
    'nama' : 'Dika',
    'umur' : 20,
    'kota' : 'Medan'
}

with open('6_Python Standard Library/Working with CSV and JSON files/JSON/test.json', 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)