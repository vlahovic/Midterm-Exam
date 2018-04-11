"""
===================   TASK 3   ====================
* Name: Negative and Non-Negative Elements
*
* Write a script that will populate a list with as
* many elements as user defines. For taken number
* of elements the script should take the input from
* user for each element. You should expect that
* user will always provide integer numbers. At the
* end, the script should print how many negative
* and non-negative numbers there were present in
* the list.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

n = int(input("Koliko brojeva unosite? "))# da bi znali kolika ce biti duzina liste(mora biti cijeli broj)

lista = [] # na pocetku je data prazna lista

nenegativni = negativni = 0

for i in range(n):  # koliko lista ima clanova, toliko cemo puta pitati korisnika da unese novi clan liste
    novi_broj = int(input("Unesite "+ str(i+1)+ ".broj: ")) # stringovi mogu da se spoje sabiranjem
    lista.append(novi_broj) # svaki od unijetih brojeva dodajemo u listu

    if novi_broj < 0: # ako je unijeti broj manji od nule, ukupan broj negativnih se uveca za 1
        negativni += 1

    else:             # u suprotnom se uveca broj nenegativnih za 1
        nenegativni += 1

print("Vasa lista: ", str(lista))
print("Nenegativnih brojeva u listi ima: ", nenegativni)
print("Negativnih brojeva u listi ima: ", negativni)