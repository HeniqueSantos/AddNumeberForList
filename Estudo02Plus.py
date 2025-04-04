#Versao 0.2 Do meu Adicionar Numeros

import time

listaDeNumeros = []

print('\nBem-Vindo ao Gerenciador de Numeros')

def mostrarMenu():
    time.sleep(1)
    """Mostra as opções ao usuário"""

    print('\n=============MENU==============')
    print('1 - Adicionar Numero')
    print('2 - Remover Numero')
    print('3 - Mostrar Lista')
    print('4 - Sair')


    

while True:
    mostrarMenu()
    opcao = input('Escolha uma opcao: ').strip()

    # Adicionar um numero na Lista
    if opcao == '1':
        while True:
            try:
                numero = input('Digite um número para adicionar (ou digite "Exit" para voltar) : ')
                if numero.upper() == 'EXIT':
                    break
                    
                numero = int(numero)
                if numero in listaDeNumeros:
                    print("Esse número já foi adicionado à sua lista!")
                    time.sleep(1)
                else:
                    listaDeNumeros.append(numero)  
                    print(f'{numero} foi adicionado a Lista!')
                    time.sleep(0.5)
            except ValueError:
                print('Digite um número válido! Tente novamente.')
                time.sleep(1)

    # Remover um numero da Lista            
    elif opcao == '2':
        while True:
            try:
                numero = input('Digite um número para remover (ou "EXIT" para voltar, "LISTA" para exibir a lista):')
                if numero.upper() == 'EXIT':
                    break
                elif numero.upper() == 'LISTA': 
                    print(f'Sua lista de números é {listaDeNumeros}')
                    time.sleep(1)
                    continue

                numero = int(numero)
                if numero in listaDeNumeros:
                    listaDeNumeros.remove(numero)
                    print(f'{numero} removido com sucesso!')
                    time.sleep(0.5)
                else:
                    print('Número não encontrado na lista! Tente novamente.')
                    print(f'Sua lista de números é {listaDeNumeros}')
                    time.sleep(0.5)
            except ValueError:
                print('Digite um numero valido! Tente novamente.')
                time.sleep(0.5)

    # Mostrar lista           
    elif opcao == '3':
        if not listaDeNumeros:
            print('Sua lista está vazia!')
            time.sleep(3)
        else:
            print(f'Sua lista de números é {listaDeNumeros}')
            time.sleep(3)

    # Encerar o executor
    elif opcao == '4':
        break