d = {
    'Hendrix': '1942',
    'Allman': '1946',
    'King': '1925',
    'Clapton': '1945',
    'Johnson': '1911',
    'Berry': '1926',
    'Vaughan': '1954',
    'Cooder': '1947',
    'Page': '1944',
    'Richards': '1943',
    'Hammett': '1962',
    'Cobain': '1967',
    'Garcia': '1942',
    'Beck': '1944',
    'Santana': '1947',
    'Ramone': '1948',
    'White': '1975',
    'Frusciante': '1970',
    'Thompson': '1949',
    'Burton': '1939',
}

# Sort the dictionary by year in ascending order, then alphabetically
sorted_names = sorted(d.keys(), key=lambda x: (d[x], x))

# Display the sorted names without the year
for name in sorted_names:
    print(name)
