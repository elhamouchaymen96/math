# PGCD(a,b,c)
a = int(input("Entrer le premier nombre : "))
b = int(input("Entrer le deuxième nombre : "))
c = int(input("Entrer le troisième nombre : "))

print("\n--- Calcul du PGCD(a, b) ---")

# PGCD(a, b)
while b != 0:
    r = a % b
    print("a =", a, ", b =", b, "=> r = a % b =", r)
    a = b
    b = r

# Maintenant a contient PGCD(a, b)
pgcd_ab = a
print("PGCD(a, b) =", pgcd_ab)

print("\n--- Calcul du PGCD(PGCD(a, b), c) ---")

# PGCD(PGCD(a, b), c)
a = pgcd_ab   # remettre le résultat dans a
b = c         # comparer avec c

while b != 0:
    r = a % b
    print("a =", a, ", b =", b, "=> r = a % b =", r)
    a = b
    b = r

# Résultat final
print("\nPGCD des trois nombres =", a)
