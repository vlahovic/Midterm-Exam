"""
===================   TASK 4   ====================
* Name: Convert To Upper
*
* Write a function `convert_2_upper` that will take
* a string as an argument. The function should
* convert all lowercase letter to uppercase without
* usage of built-in function `upper()`.

* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""
def convert_2_upper(recenica):

    if not isinstance(recenica,str): #provjeravo da li je unijet string
        print("Pogresan unos!")

    nova_recenica = ''  #data recenica ispisana velikim slovima, koju treba da dobijemo, je na pocetku prazna

    for karakter in recenica: # prolazimo kroz svaki karakter u recenici
        broj_chr = ord(karakter) # svaki karakter pretvaramo u ASCII kod tj. odgovarajuci broj
        if broj_chr > 96 and broj_chr < 123: # mala slova u ASCII kodu pocinju sa 97 i zavrsavaju sa 122, a velika su od 65 do 90
                                # pa svako slovo date recenice ciji odgovarajuci broj u ASCII kodu odgovara malom slovu
                                # smanjicemo za 32 i dobiti njemu odgovarajuce veliko slovo

            broj_velikog_slova = broj_chr - 32
            karakter = chr (broj_velikog_slova) # vratimo broj u odgovarajuce slovo

        nova_recenica += karakter # karakter po karakter dodajemo u novu recenicu

    return nova_recenica # f-ja vraca novu recenicu, koja je sada ispisana velikim slovima

def main():

    recenica="IvaNa KONatAr 17/115"
    print("Data recenica napisana velikim slovima : ", convert_2_upper(recenica))
    pass

main()