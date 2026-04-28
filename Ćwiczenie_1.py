slowa= ["kajak", "butelka", "długopis", "anna", "woda"]
sprawdzenie = list(map(lambda s: s == s[::-1], slowa))
print(sprawdzenie)
