print('fogo, gelo, água, voador')
nome = str(input('Escolha um golpe: '))

print('Ensolarado, Nevando, Chovendo, Ventando')
clima = str(input('Escolha um clima: '))

print('10, 20, 30, 40')
poder = float(input('Digite o poder: '))

if(nome == "fogo" and clima == "Ensolarado"):
    print("{}".format(poder * 1.5))

elif(nome == "gelo" and clima == "Nevando"):
    print("{}".format(poder * 1.1))

elif(nome == "água" and clima == "Chovendo"):
    print("{}".format(poder * 2.1))

elif(nome == "voador" and clima == "Ventando"):
    print("{}".format(poder * 0.5))

else:
    print("{}".format(poder))

