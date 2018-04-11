"""
===================   TASK 5   ====================
* Name: Del Boy Millionaire
*
* Help Del Boy become a millionaire. Del Boy is
* trading bitcoins on crypto-exchanges with simple
* algorithm. He is buying where the price of bitcoin
* is the lowest and selling where the bitcoin is
* the most expensive. Write a function `get_profit`
* which will take a list of bitcoin prices in USD as
* argument. The function should return what is the
* maximum possible profit for given bitcoin prices
* on different exchanges.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def get_profit(lista):  # najveci moguci profit koji mozemo ostvariti cemo preracunati


# kada najmanju trenutnu vrijednost bitcoin-a oduzmemo od najvece

def min(lista):  # defisemo funkcije min i max

    min_lista = lista[0]  # fiksiramo prvi clan liste, tj postavimo da je on najmanji

    for i in range(len(lista) - 1):  # prolazimo kroz ostale clanove liste; onaj sto smo fiksirali iskljucujemo
        # pa zato pozicija prvog clana u listi kroz koji prolazimo je i+1

        if min_lista > lista[i + 1]:  # ako je clan kroz koji prolazimo manji od datog minimuma, sada on postaje minimum
            min_lista = lista[i + 1]

    return min_lista  # f-ja vrace minimum liste


def max(lista):  # analogno kao za minimum

    max_lista = lista[0]

    for i in range(len(lista) - 1):

        if max_lista < lista[i + 1]:
            max_lista = lista[i + 1]

    return max_lista


return max(lista) - min(lista)  # na kraju f-ja get_profit vrace razliku najvece i najmanje vrijednosti


def main():
    lista = [11283.5, 10221, 9896.6]
    print("Najveci ostvareni profit je: ", get_profit(lista))
    pass


main()