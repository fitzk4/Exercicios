pecasLista = []

def cadastrarPeca(codigo):
    print('Selecionada a opção "Cadastrar peça"')
    print('O código da peça é: {:0>3}'.format(codigo))
    nome = input('Entre com o nome da peça: ')
    fabricante = input('Entre com o fabricante da peça: ')
    valor = float(input('Entre com o valor em R$ da peça: '))
    pecasDicionario = {'codigo': codigo, 'nome': nome, 'fabricante': fabricante, 'valor': valor}
    pecasLista.append(pecasDicionario.copy())

def consultarPeca():
    while True:
        try:
            print('Você selecionou a opção de consultar peças')
            opConsultar = int(input('Entre com a opção desejada\n'
                                    '1 - Consultar todas as peças\n'
                                    '2 - Consultar por código\n'
                                    '3 - Consultar por fabricante\n'
                                    '4 - Retornar\n ---> '))
            if opConsultar == 1:
                print('-' * 20)
                for pecas in pecasLista:
                    for key, value in pecas.items():
                        print('{}: {}'.format(key, value))
                    print('-' * 20)
            elif opConsultar == 2:
                print('Você selecionou consultar por código')
                entrada = int(input('Digite o código: '))
                print('-' * 20)
                for pecasDicionario in pecasLista:
                    if pecasDicionario['codigo'] == entrada:
                        for key, value in pecasDicionario.items():
                            print('{}: {}'.format(key, value))
                        print('-' * 20)
            elif opConsultar == 3:
                print('Você selecionou consultar por fabricante')
                entrada = input('Digite o fabricante: ')
                print('-' * 20)
                for pecasDicionario in pecasLista:
                    if pecasDicionario['fabricante'] == entrada:
                        for key, value in pecasDicionario.items():
                            print('{}: {}'.format(key, value))
                        print('-' * 20)
            elif opConsultar == 4:
                break
            else:
                print('Favor digitar somente as opções válidas!')
                continue
        except ValueError:
            print('Pare de inventar opções!')
            continue

def removerPeca():
    print('Você selecionou remover peça')
    entrada = int(input('Digite o código da peça para remover'))
    for pecas in pecasLista:
        if(pecas['codigo'] == entrada):
            pecasLista.remove(pecas)
    else:
        print('Você removeu o código')

print('Bem vindo ao controle de estoque de peças!')
registroPecas = 0

while True:
    try:
        opcao = int(input('Selecione uma opção:\n'
                            '1 - Cadastrar Peças\n'
                            '2 - Consultar Peças\n'
                            '3 - Remover Peças\n'
                            '4 - Sair\n --->'))
        
        if opcao == 1:
            registroPecas = registroPecas + 1
            cadastrarPeca(registroPecas)
        elif opcao == 2:
            consultarPeca()
        elif opcao == 3:
            removerPeca()
        elif opcao == 4:
            print('Programa finalizado')
            break
        else:
            print('Digite somente opções válidas!')
            continue
    except ValueError:
        print('Pare de inventar opções!')



