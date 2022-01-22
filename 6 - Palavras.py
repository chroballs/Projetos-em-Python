lista = []

while True:
    lista.append(input("Adicione palavras a sua lista pessoal: "))
    resp = str(input("1. Excluir palavras repetidas | 2.Excluir palavras com R [1/2]"))
    if resp == "2":
        for Rr in lista:
            lista.remove(Rr)
            print(lista)    

    elif resp == "1":
        repetidos = list(set(lista))
        repetidos
        print(repetidos)

