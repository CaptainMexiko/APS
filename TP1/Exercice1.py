#!/usr/bin/python3

# Exercice1
print("Question1")
# Creation de la Liste
listeExo1 = [17, 38, 10, 25, 72]

listeExo1.sort()
print("Liste trié :", listeExo1)

listeExo1.append(12)
print("Liste avec 12 :", listeExo1)

listeExo1.reverse()
print("Liste reverse :", listeExo1)

print("La valeur 17 est à l'index :", listeExo1.index(17))

listeExo1.remove(38)
print("Liste remove :", listeExo1)

sL1 = listeExo1[2:4]
print("Sous-liste1 :", sL1)

sL2 = listeExo1[0:2]
print("Sous-liste2 :", sL2)

sl3 = listeExo1[3:len(listeExo1)]
print("sous-liste3 :", sl3)

sl4 = listeExo1[0:len(listeExo1)]
print("sous-liste4 :", sl4)

last = listeExo1[-1]
print("dernier elem :", last)

print("Question2")
for i in range(4):
    print("La range est :", i)
    pass

print("\n")

for i in range(4, 8):
    print("La range est :", i)
    pass

print("\n")

for i in range(2, 9, 2):
    print("La range est :", i)
    pass

print("Question3")
chose = list(range(0, 6))
print(3 in chose)
print(6 in chose)

print("Question4-5")
compr1 = [i + 3 for i in range(6)]
print("Liste en compréhension 1", compr1)

compr2 = [i + 3 if i >= 2 else i for i in range(6)]
print("Liste en compréhension 2", compr2)

print("Question6")


def compterMots(input):
    mots = input.split(' ')
    print(mots)
    dico = {}
    for i in mots:
        if i not in dico:
            dico[i] = mots.count(i) / len(mots)
            pass
        pass
    print(dico)
    pass


compterMots("boi tu la de la re de tu boi fer tu la de re de boi boi")


def nmbS():
    nbD = 11
    while int(nbD) > 10:
        print("Donner le nombre de dés")
        nbD = input()
        pass
    nbD6 = int(nbD) * int(6)
    print("Donner la somme comprise entre", nbD, "et", nbD6)
    somme = input()
    if int(somme) > (int(nbD) * int(6)) or int(somme) < int(nbD):
        print("Calcul impossible, donnée erronée")
        exit(0)
    pass


nmbS()
