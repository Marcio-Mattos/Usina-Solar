# Dimensionamento de um sistema votofoltaico.

# Em função do consumo médio residencial, dimensionar a potência necessária (potência dos painéis)

# a ser instalada para atender a necessidade do consumo de energia.


class BD: # verifica se a função já foi criada. Caso, sim, não criará novamente.

    def cria_BD(cliente): # cria banco de dados

        arquivo = open('bancodedados.txt','w')

        arquivo.close()


def cadastrar_projeto():

        
    cliente = input('Nome do cliente: ')

    endereco = input('Endereço: ')

    numero = int(input('Número: '))

    num = str(numero) # para usar no arquivo texto

    resptec = input('Responsál técnico: ')

    consanual = float(input('Informe o consumo anual em (Kwh): '))

    consanuall = str(consanual)# para usar no arquivo texto

    medpotmensal = consanual/12

    medpotmensal = round(medpotmensal,2) # arredonda 2 casas decimais

    medpotmensall = str(medpotmensal)# para usar no arquivo texto

    print('Média consumo mensal:',medpotmensal, 'Kwh.')

    potdia = medpotmensal/24

    potdia = round(potdia,2) # arredonda 2 casas decimais
     
        
    print('Média consumo diário:',potdia, 'Kwh.')

    hsolpleno = float(input('Informe as horas de sol pleno: '))

    potinstal = potdia/hsolpleno

    potinstal = round (potinstal,2) # arredonda 2 casas decimais

    potinstall = str(potinstal)# para usar no arquivo texto

          
    print('Potência a ser instalada:',potinstal, 'Kwp.')

    print()

    arquivo = open('bancodedados.txt','a')

    arquivo.write(cliente.title() +':') # grava primeiras letras em maiúscula

    arquivo.write(endereco.title() +':')

    arquivo.write(num + ':')

    arquivo.write(resptec.title() +':')

    arquivo.write(consanuall + ':')

    arquivo.write(medpotmensall + ':')

    arquivo.write(potinstall + '\n')

    arquivo.close()

    print()
   

def consulta_cadastro():
    

    opcao = int(input('Que tipo de consulta deseja fazer?\n1) Completa.\n2) Unica,\n >'))

    if (opcao == 1):

        arquivo = open ('bancodedados.txt').readlines()

        arquivo = [str(x).rstrip() for x in arquivo] # "srt(x)" converte valores dentro do arquivo em valores exatos. "rstrip" remove espaços entre as linhas

        for linha in arquivo:

            print(linha)

        print()
               

def main():

      
    print('='*40)

    print('     Dimensionamento sistema solar')

    print('='*40)
    

    op = -1

    while op != 3:

        print('='*40)

        print(' Escolha uma das opções.\n 1) Cadastrar projeto,\n 2) Consultar cadastro.\n 3) Sair')

        print('='*40)

        op = int(input('Opção:')) # Escolher opção

        if op == 1:

            cadastrar_projeto()

        elif op == 2:

            consulta_cadastro()

        elif op == 3:

            print('Até o próximo projeto !!')

           
main()
    

          
          
