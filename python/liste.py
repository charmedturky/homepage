einkaufs_liste = ["Milch","Eier","Backpulver","Nuttela","Mehl"]

for val in einkaufs_liste:
    print(val)

einkaufs_liste[0] = "Saft"
print(einkaufs_liste[0])

freund = ["Paulo", "Barros", 12]
pedro = ["Pedro", "Venancio", 11]
martin = ["Martin", "Koppitz", 12]

alle_freunde = [freund, pedro]
alle_freunde.append(martin)

summe = 0

for val in alle_freunde:
    print(val)
    summe = summe + val[2]

print(summe)

paulo = {
    'name': 'Paulo',
    'lastname': 'Barros'
    'age': 12
}
print(papa['name',"lastname", "age"])

PV = {
    'name': 'Pedro',
    'lastname': 'Venancio'
    'age': 11
}
print(PV['name',"lastname", "age"])

martin = {
    'name': 'Martin',
    'lastname': 'Koppitz'
    'age': 12
}
print(martin['name',"lastname", "age"])