import random as rd
import time

#function to up the randomness to the cpu choice
def sd():
    motherlist = []
    lista0 = rd.choice(['pedra', 'papel', 'tesoura'])
    motherlist.append(lista0)

    lista1 = rd.choice(['pedra', 'tesoura', 'papel'])
    motherlist.append(lista1)

    lista2 = rd.choice(['papel', 'tesoura', 'pedra'])
    motherlist.append(lista2)

    lista3 = rd.choice(['papel', 'pedra', 'tesoura'])
    motherlist.append(lista3)

    lista4 = rd.choice(['tesoura', 'pedra', 'papel'])
    motherlist.append(lista4)

    lista5 = rd.choice(['tesoura', 'papel', 'pedra'])
    motherlist.append(lista5)

    choice = rd.choice(motherlist)
    return choice


nome = str(input('Insira o nick do player: '))
pontC = 0
pontP = 0

while True:
    comp = sd()
    player = str(input('\nPedra, papel, ou tesoura, qual sua escolha? ')).strip().lower()

    for c in range(0,3):
        print(f'{c+1} . . .')
        time.sleep(1)
    print(f'\nA máquina escolheu: {comp}')

    if player == comp:
        print('\n\033[34m- - - EMPATE - - -\033[m\n')
    elif player == 'tesoura' and comp == 'papel':
        print(f'\n\033[35m- - - Vitória do {nome} - - -\033[m\n')
        pontP += 1
    elif comp == 'tesoura' and player == 'papel':
        print(f'\n\033[31m- - - Vitória da máquina - - -\033[m\n')
        pontC += 1
    elif player == 'papel' and comp == 'pedra':
        print(f'\n\033[35m- - - Vitória do {nome} - - -\033[m\n')
        pontP += 1
    elif comp == 'papel' and player == 'pedra':
        print(f'\n\033[31m- - - Vitória da máquina - - -\033[m\n')
        pontC += 1
    elif player == 'pedra' and comp == 'tesoura':
        print(f'\n\033[35m- - - Vitória do {nome} - - -\033[m\n')
        pontP += 1
    elif comp == 'pedra' and player == 'tesoura':
        print(f'\n\033[31m- - - Vitória da máquina - - -\033[m\n')
        pontC += 1

    option = str(input('Deseja continuar?(s/n) ')).strip().lower()
    if option == 'n':
        break

print(f'Pontuação final: \n\033[31mMáquina: {pontC}\033[34m \n\033[35m{nome}: {pontP}\n\033[m')
