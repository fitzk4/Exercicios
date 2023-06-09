def dimensoesObjeto():
    mult = 0
    while True:
        try:
            comp = int(input('Digite o comprimento do objeto em cm: '))
            larg = int(input('Digite a largura do objeto em cm: '))
            alt = int(input('Digite a altura do objeto em cm: '))
            a = float(comp * larg * alt)
            print('O volume calculado do objeto é de: {:.2f}Cm³'.format(a))
            if(a > 0) and (a < 1000.0):
                return 10.00
            elif(a >= 1000.0) and (a < 10000.0):
                return 20.00
            elif(a >= 1000.0) and (a < 100000.0):
                return 50.00
            else:
                print('Objeto não tem o tamanho aceitável!\n'
                      'Entre com as dimensões novamente ')
                continue
        except ValueError:
            print('Valor digitado não numérico!\n'
                  'Entre com as dimensões novamente')
            continue
            
def pesoObjeto():
    while True:
        try:
            peso = float(input('Digite o peso do objeto em KG: '))
            p = peso
            if(p > 0) and (p <= 0.1):
                return 1
            elif(p >= 0.11) and (p <= 1):
                return 1.5
            elif(p <= 10) and (p >= 1.10):
                return 2
            elif(p <= 30) and (p >= 10.1):
                return 3
            else:
                print('Objeto excede o peso aceitável!')
                continue
        except ValueError:
            print('Valor digitado não numérico\n'
                  'Entre com o peso desejado novamente')
            continue

def rotaObjeto():
    while True:
        try:
            rota = (input('Selecione a rota desejada: \n'
                          'RS - De Rio de Janeiro até São paulo\n'
                          'SR - De São Paulo até Rio de Janeiro\n'
                          'BS - De Brasília até São Paulo\n'
                          'SB - De São Paulo até Brasília\n'
                          'BR - De Brasília até São Paulo\n'
                          'RB - Rio de Janeiro até Brasília\n'
                          'Escolha uma rota: '))
            if (rota == 'RS') or (rota == 'rs'):
                return 1
            elif (rota == 'SR') or (rota == 'sr'):
                return 1
            elif (rota == 'BS') or (rota == 'bs'):
                return 1.2
            elif (rota == 'SB') or (rota =='sb'):
                return 1.2
            elif (rota == 'BR') or (rota == 'br'):
                return 1.5
            elif (rota == 'RB') or (rota == 'rb'):
                return 1.5
            else:
                print('Código inexistente!')
                continue
        except ValueError:
            print('Código inexistente! \n'
                  'Por favor entre com a rota desejada novamente!')
            continue

print('Bem vindo a companhia de logistica!')

area = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
valor = (area * peso * rota)

print('Total a pagar: R$ {:.2f} - (Dimensões: {} * Peso: {} * Rota: {})'.format(valor,area,peso,rota))
