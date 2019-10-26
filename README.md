# Usina-Solar
Dimensionamento de um sistema de geração de energia fotovoltaica.
# Dimensionamento de um sistema votofoltaico.

# Em função do consumo médio residencial, dimensionar a potência necessária

# a ser instalada.

print('*'*40)

print('     Dimensionamento Sistema Solar')

print('*'*40)

print()

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

print('*'*40)

print(projetos)

print('*'*40)

print('<<< FIM >>>')
