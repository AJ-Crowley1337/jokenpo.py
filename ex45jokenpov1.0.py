from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('''\033[1;34mSuas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogada = int(input('Qual é a sua jogada? '))
jogador = jogada - 1
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('–=' * 21)
print(f'Computador jogou:\033[m \033[1;31m{itens[pc]}\033[m')
if jogador <= 3:
    print(f'\033[1;34mJogador jogou:\033[m \033[1;31m{itens[jogador]}\033[m')
else:
    print('\033[7;37mJOGADA INVÁLIDA!\033[m')
print('\033[1;34m-=\033[m' * 21)
if pc == 0:
    if jogador == 0:
        print('\033[1;35mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[1;33mVocê VENCEU!!\033[m')
    elif jogador == 2:
        print('\033[1;31mVocê PERDEU!!\033[m')
    else:
        print('\033[1;31;47mJOGADA INVÁLIDA!\033[m')
elif pc == 1:
    if jogador == 0:
       print('\033[1;31mVocê PERDEU!!\033[m')
    elif jogador == 1:
       print('\033[1;35mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[1;33mVocê VENCEU!!\033[m')
    else:
        print('\033[1;31;47mJOGADA INVÁLIDA!\033[m')
elif pc == 2:   
    if jogador == 0:
        print('\033[1;33mVocê VENCEU!!\033[m')
    elif jogador == 1:
        print('\033[1;31mVocê PERDEU!!\033[m')   
    elif jogador == 2:
        print('\033[1;35mEMPATE!\033[m')
    else:
        print('\033[1;31;47mJOGADA INVÁLIDA!\033[m')
print('\033[1;34m-=\033[m' * 21)
