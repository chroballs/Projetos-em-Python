questionario = []

questionario.append(input("Telefonou para a vítima? 1. Sim | 2. Não"))
questionario.append(input("Esteve no local do crime? 1. Sim | 2. Não"))  
questionario.append(input("Mora perto da vítima? 1. Sim | 2. Não"))    
questionario.append(input("Devia para a vítima? 1. Sim | 2. Não"))         
questionario.append(input("Já trabalhou com a vítima? 1. Sim | 2. Não"))

answer = 0

for i in questionario:
    answer += int(i)
if(answer == 3):
    print('VOCÊ É SUSPEITO!')
elif(answer == 4):
    print('VOCÊ FEZ PARTE DO CRIME!')
elif(answer == 5):
    print('VOCÊ FEZ PARTE DO CRIME!')
else:
    print('VOCÊ É INOCENTE!')
