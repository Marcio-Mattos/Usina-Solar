# Dimensionamento de um sistema votofoltaico.

# Em função do consumo médio residencial, dimensionar a potência necessária

# a ser instalada.


def novoprojeto():

    projeto = {}

    projetos = []


    while True:

        projeto.clear()
        
        projeto['cliente'] = input('Nome do cliente: ')

        projeto['endereco'] = input('Endereço: ')

        projeto['resptec'] = input('Responsál técnico: ')

        projeto['medpotmensal'] = float(input('Informe a média do consumo mensal em KWh: '))

        hsolpleno = float(input('Informe as horas de sol pleno: '))

        potdia = projeto['medpotmensal']/24

        projeto['potinstal'] = potdia/hsolpleno

        projetos.append(projeto.copy())

        while True:

            resp = input('Deseja continuar? [S/N]: ').upper()[0]

            if resp in 'SN':

                break

            print('ERRO ! Digite [S] ou [N].')

        if resp == 'N':

            break

    return projetos

def selprojeto(): # selecionar projeto

    print('Iniciando teste')

def main():

    print('*'*40)

    print('     Dimensionamento Sistema Solar')

    print('*'*40)

    print()

    print('Selecione as opções abaixo:')

    print()

    print('*'*30)

    print('1 - Novo projeto.')

    print()

    print('2 - Selecionar projeto.')

    print()

    print('0 - Sair.')

    print('*'* 30)

    op = -1 # artifício para iniciar
    
    while op != 0:

        op = int(input('Digite a opção: '))

        print()

        if op == 1:

            print(novoprojeto())

        elif op == 2:

            selprojeto()
           

        elif op == 0:

            break

main()





