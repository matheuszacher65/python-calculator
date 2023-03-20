import time
import os

lista_soma = []
lista_sub = []
lista_mult = []
lista_div = []
lista_expo = []


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('----- CALCULADORA ------\n')
    print('1 : Soma')
    print('2 : Subtração')
    print('3 : Multiplicação')
    print('4 : Divisão')
    print('5 : Exponenciação')
    print('9 : Sair')
    item = input('\nEscolha a opção que deseja realizar: ')
    return item


def soma():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n.:: SOMA ::.')
    print('\nDigite a quantidade de números que quiser.')
    print('>>> Para encerrar, digite "P".\n')
    
    seq = 1
    lista_soma.clear()

    while True:
        num = input('{}º número: ' .format(seq))
        if num == 'p' or num == 'P':
            break
        else:
            lista_soma.append(float(num))
        seq += 1

    print('')
    print('Resultado ->', sum(lista_soma))

    print('\nFazer outra soma - 1 / Voltar ao menu - 0')
    pos_operacao = input()
    
    while pos_operacao not in '10':
        print('\nResposta inválida')
        pos_operacao = input('>>> Fazer outra soma - 1 / Voltar ao menu - 0')

    if pos_operacao == '1':
        soma()
    elif pos_operacao == '0':
        pass

    return (sum(lista_soma))


def sub():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n.:: SUBTRAÇÃO ::.')
    print('\nDigite a quantidade de números que quiser.')
    print('>>> Para encerrar, digite "P".\n')
    
    seq = 1
    lista_sub.clear()

    while True:
        num = input('{}º número: ' .format(seq))
        if num == 'p' or num == 'P':
            break
        else:
            lista_sub.append(float(num))
        seq += 1

    print('')
    print('Resultado ->', lista_sub[0] - sum(lista_sub[1:]))
    input('\nPressione ENTER para voltar ao menu.')

    return (lista_sub[0] - sum(lista_sub[1:]))


def mult():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n.:: MULTIPLICAÇÃO ::.')
    print('\nDigite a quantidade de números que quiser.')
    print('>>> Para encerrar, digite "P".\n')
    
    seq = 1
    lista_mult.clear()

    while True:
        num = input('{}º número: ' .format(seq))
        if num == 'p' or num == 'P':
            break
        else:
            lista_mult.append(float(num))
        seq += 1

    resultado_mult = lista_mult[0]
    for i in lista_mult[1:]:
        resultado_mult *= i
    
    print('')
    print('Resultado ->', resultado_mult)
    input('\nPressione ENTER para voltar ao menu.')

    return resultado_mult


def div():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n.:: DIVISÃO ::.')
    print('\nDigite a quantidade de números que quiser.')
    print('>>> Para encerrar, digite "P".\n')
    
    seq = 1
    lista_div.clear()

    while True:
        num = input('{}º número: ' .format(seq))
        if num == 'p' or num == 'P':
            break
        else:
            lista_div.append(float(num))
        seq += 1

    resultado_div = lista_div[0]
    for i in lista_div[1:]:
        resultado_div /= i
    
    print('')
    print('Resultado ->', resultado_div)
    input('\nPressione ENTER para voltar ao menu.')

    return resultado_div


def expo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n.:: EXPONENCIAÇÃO ::.')
    print('\nDigite a quantidade de números que quiser.')
    print('>>> Para encerrar, digite "P".\n')
    
    seq = 1
    lista_expo.clear()

    while True:
        num = input('{}º número: ' .format(seq))
        if num == 'p' or num == 'P':
            break
        else:
            lista_expo.append(float(num))
        seq += 1

    resultado_expo = lista_expo[0]
    for i in lista_expo[1:]:
        resultado_expo **= i
    
    print('')
    print('Resultado ->', resultado_expo)
    input('\nPressione ENTER para voltar ao menu.')

    return resultado_expo


# Processamento do menu e chamada das funções
if __name__ == '__main__':

    escolha = '0'   # -> Precisa botar isso pq senão dá o erro "escolha not defined", já que escolha só vai atribuir um valor quando a func menu() for chamada, mas ela está dentro do while.
                    # -> Antes do while, não sabemos o que é "escolha", pq ela só é definida quando chamamos a func menu(), e o while precisa de algo para comparar o seu booleano.
    x = '0'

    while escolha != '9':
        if x == '0':
            escolha = menu()

        if escolha == '1':
            soma()
        elif escolha == '2':
            sub()
        elif escolha == '3':
            mult()
        elif escolha == '4':
            div()
        elif escolha == '5':
            expo()
        elif escolha == '9':
            print('\nSaindo...')
            time.sleep(2)
        else:
            print('\nOpção desconhecida!')
            input('--> Pressione ENTER para continuar.')