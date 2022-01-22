from random import randint
maos = ('Pedra', 'Papel', 'Tesoura')
jogador1 = int(input('Qual é a sua jogada?'))
jogador2 = int(input('Qual é a sua jogada?'))
print('-=' * 20)
print('Jogador 1 jogou {}'.format(maos[jogador1]))
print('Jogador 2 jogou {}'.format(maos[jogador2]))
print('-=' * 20)
if jogador1 == 0:
    if jogador2 == 0:
        print('EMPATE!')
    elif jogador2 == 1:
        print('JOGADOR 2 GANHOU!')
    elif jogador2 == 2:
        print('JOGADOR 1 GANHOU!')
    else:
        print('JOGADA INVALIDA')
###############################
elif jogador1 == 1:
    if jogador2 == 0:
        print('JOGADOR 1 GANHOU!')
    elif jogador2 == 1:
        print('EMPATE!')
    elif jogador2 == 2:
        print('JOGADOR 2 GANHOU!')
    else:
        print('JOGADA INVALIDA')
elif jogador1 ==2:
    if jogador2 == 0:
        print('JOGADOR 1 GANHOU!')
    elif jogador2 == 1:
        print('JOGADOR 2 GANHOU!')
    elif jogador2 == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA')
