# Lista

Numeros = []

print('Se voce deseja encerrar o app, a qualquer momento, digite "1"')
print('Lista atual:', Numeros)

while True:

   
    

    pergunta = input('Voce deseja adicionar ou remover um numero? (adicionar/remover) ')

    if pergunta == 'adicionar':

        numero = int(input('\n Digite o numero que deseja adicionar: '))
        Numeros.append(numero)
        print('Numero adicionado. \n')
        print('Lista atualizada:', Numeros)

    elif pergunta == 'remover':

        print('Lista atual:', Numeros)
        remover = int(input('Digite o numero que deseja remover: '))
        Numeros.remove(remover)
        print('Numero removido. \n')

    elif pergunta == '1' :
        break

    else:
        print('Opcao invalida. \n')
        print('Lista atual:', Numeros)
        continuar = input('Deseja continuar? (sim/nao) ')
        if continuar == 'nao':
            break

print
print(f'A lista final e : {Numeros}')