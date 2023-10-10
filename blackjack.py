import random as rd

print('\033[1;35mBEM VINDO(A) À MESA DE BLACKJACK')
print('\nAs regras são simples: \nDuas cartas iniciais com 2 valores somados \nPeça cartas ou pare no valor \nA mesa deve pegar cartas até atingir o valor mínimo 17 ou 21 \nGanha se seu valor for 21 ou maior q o da mesa\033[m')

while True:
    cor = rd.choice(['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m'])
    print(cor)
    n1 = int(rd.randint(1, 11))
    n2 = int(rd.randint(1, 10))
    bj = n1 + n2
    print(f'\nCartas: {n1} e {n2} \nSoma: {bj}')

    while True:
        if bj == 21:
            print('BLACKJACK! VITÓRIA DO USUÁRIO!')
            break

        option1 = str(input('\nPedir carta ou parar?(C/P) ')).upper().strip()
        if option1 == 'C':
            n3 = rd.randint(1, 10)
            bj += n3
            print(f'\nCarta recebida: {n3} \nSoma: {bj}')
            if bj > 21:
                print('\nVITÓRIA DA MESA! USUÁRIO ULTRAPASSOU 21!\n')
                break
            elif bj == 21:
                print('\nVITÓRIA DO USUÁRIO COM 21!\n')
                break
        
        elif option1 == 'P':
            print('\nRevelando cartas da mesa!')
            m1 = rd.randint(1, 11)
            m2 = rd.randint(1, 10)
            bjm = m1 + m2
            print(f'\nCartas: {m1} e {m2}')
            if bjm == 21:
                print('\nBLACKJACK! A mesa venceu com 21!\n')
                break
            else:
                while bjm < 17:
                    m3 = rd.randint(1, 10)
                    bjm += m3
                    print(f'Carta: {m3} (soma: {bjm})')
                if bjm > bj and bjm <= 21:
                    print(f'\nVITÓRIA DA MESA COM {bjm}!\n')
                    break
                elif bjm < bj and bjm > 17:
                    print(f'\nVITÓRIA DO USUÁRIO COM {bj}!\n')
                    break
                elif bjm == bj and bjm > 17:
                    print(f'\nSomatório: {bjm}\n')
                    print('\nEMPATE!\n')
                    break
                elif bjm == 17:
                    if bjm > bj:
                        print(f'\nVITÓRIA DA MESA COM {bjm}!\n')
                    else:
                        print(f'\nVITÓRIA DO USUÁRIO COM {bj}!\n')
                    break
                elif bjm > 21:
                    print(f'\nVITÓRIA DO USUÁRIO, A MESA ULTRAPASSOU 21!\n')
                    break

        else:
            print('Insira uma opção válida!')
    print('\033[m')
    option2 = str(input('Deseja jogar novamente?(S/N) ')).strip().upper()
    if option2 == 'N':
        print('\n\033[1;31mAté uma próxima partida!\033[m')
        break
