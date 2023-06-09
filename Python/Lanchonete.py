print('Bem vindo a lanchonete')

print('******************Cardápio******************')
print('| Código |          Descrição      | Valor |')
print('|  100   |      Cachorro Quente    |  9,00 |')
print('|  101   |   Cachorro Quente Duplo | 11,00 |')
print('|  102   |          X-Egg          | 12,00 |')
print('|  103   |          X-Salada       | 12,00 |')
print('|  104   |          X-Bacon        | 14,00 |')
print('|  105   |          X-Tudo         | 17,00 |')
print('|  200   |     Refrigerante lata   |  5,00 |')
print('|  201   |         Chá Gelado      |  4,00 |')

conta = 0 
opcao = 1

while opcao == 1:
    preco = 0
    produto = ''
    codigo = int(input('Digite o código do produto desejado: '))
    if codigo == 100:
        preco = 9
        produto = 'Cachorro Quente'
    elif codigo == 101:
        preco = 11
        produto = 'Cachorro Quente Duplo'
    elif codigo == 102:
        preco = 12
        produto = 'X-Egg'
    elif codigo == 103:
        preco = 12
        produto = 'X-Salada'
    elif codigo == 104:
        preco = 14
        produto = 'X-Bacon'
    elif codigo == 105:
        preco = 17
        produto = 'X-Tudo'
    elif codigo == 200:
        preco = 5
        produto = 'Refrigerante lata'
    elif codigo == 201:
        preco = 4
        produto = 'Chá gelado'
    else:
        print('Código ou produto inválido!')
        continue
    print('Você pediu um {} no valor de R${:.2f}'.format(produto,preco))
    conta = conta + preco
    novopedido = 2
    while novopedido != 1 and novopedido != 0:
        print('Deseja pedir mais alguma coisa? ')
        print(' 1 - Sim ')
        print(' 0 - Não ')
        opcao = int(input(': '))
        if opcao == 1:
            novopedido = 1
            print('Continuando...')
        elif opcao == 0:
            novopedido = 0
            break
        else:
            print('Opção inválida!')
            continue
print('Total a ser pago é de: R${:.2f}'.format(conta))
