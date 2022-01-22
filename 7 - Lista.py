import random

class abobora(object):
    name = "abobora"
class abacate(object):
    name = "abacate"
class abacaxi(object):
    name = "abacaxi"
class tomate(object):
    name = "tomate"
class alface(object):
    name = "alface"
class acelga(object):
    name = "acelga"

def listadecompras():
    print("Escolha um produto.")
    selection = input("1. abobora \n2. abacate \n3. abacaxi \n4. tomate \n5. alface \n6. acelga")
    if selection == "1":
        produto = abobora
        print("R$ 7,99")
        return produto

    elif selection == "2":
        produto = abacate
        print("R$ 5,99")
        return produto

    elif selection == "3":
        produto = abacaxi
        print("R$ 4,99")
        return produto

    elif selection == "4":
        produto = tomate
        print("R$ 5,99")
        return produto

    elif selection == "5":
        produto = alface
        print("R$ 3,99")
        return produto

    elif selection == "6":
        produto = acelga
        print("R$ 4,99")
        return produto

    else:
        print("Selecione um produto por vez: 1,2,3,4,5 e 6.")
        listadecompras()

produto = listadecompras()
    

