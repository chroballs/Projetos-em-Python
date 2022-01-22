list = ['Professor', 'Raphael', 'Leal', {'n'}, {'N'}]

dammed = "Acesso Negado"

while dammed == "Acesso Negado":
    username = input("Digite um nome de usuario: ")

    if(username in list):
        print("Nome em uso!")

    elif("N" in username):
        print("Este user possui uma letra não ceita. Tente novamente!")

    elif("n" in username):
        print("Este user possui uma letra não ceita. Tente novamente!")

    else:
        list.append(username)
        yes = "Bem vindo!"
        print("Seja bem vindo!")
