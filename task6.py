"""
===================   TASK 6   ====================
* Name: Attendance Checker
*
* Write a student attendance checker script. The
* script should take, as user input, minimum
* required number of attended classes for student
* in order to take an exam. File `attendance.csv`
* contains info about students and number of
* classes they attended. Print student names, that
* do not have right to take an exam.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

sve_linije = open("attendance.csv",'r').readlines() #otvaramo fajl attendance.csv i citamo sve njegove linije

minimum = abs(int(input("Unesi broj: "))) # korisnik unosi na koliko najmanje casova je morao da prisustvuje student
                                          # da bi mogao da izadje na ispit (pozitivni cijeli broj)

lista=[] #lista onih koji ne mogu da izadju na ispit je na pocetku prazna

for linija in sve_linije: # prolazimo kroz svaku liniju fajla

    linija_bez_praznina = linija.strip()  # .strip() uklanja sve praznine u datoj liniji

    student_i_broj = linija_bez_praznina.split(',')  # .split(',') ce razdvojiti ono sto je odvojeno zarezom
                                                     # npr prva linija ce sad biti [Linus Torvalds,8]
                                            # na nultoj poziciji je ime, a na prvoj broj casova kojima je strudent prisustvovao
                                            # pa tako i postavimo

    ime_studenta = str(student_i_broj[0]) # ime studenta je string
    broj_casova = int(student_i_broj[1])  # broj casova je cijeli broj

    if broj_casova < minimum: # za svaku od linija kroz koju prodjemo, ako je broj casova u toj liniji manji od mimimalnog broja casova
                       # koji student treba da ima da bi mogao izaci na ispit, uzecemo ime studenta iz te linije i dodati ga u listu
        lista.append(ime_studenta)

print("Studenti koji ne mogu da izadju na ispit su: ",lista)