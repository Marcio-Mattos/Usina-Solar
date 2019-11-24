# Dimensionamento de um sistema votofoltaico.

# Em função do consumo médio residencial, dimensionar a potência necessária (potência dos painéis)

# a ser instalada para atender a necessidade do consumo de energia.



def cria_BD(cliente): # cria banco de dados

    arquivo = open('bancodedados.txt','w')

    arquivo.close()


def cadastrar_projeto():

        
    cliente = input('Nome do cliente: ')

    endereco = input('Endereço: ')

    numero = input('Número: ')

    num = str(numero) # para usar no arquivo texto

    resptec = input('Responsál técnico: ')

    consanual = input('Informe o consumo anual em (Kwh): ')
    
    while True:

        

        if consanual.isdigit() == True:

            break

        print('ERRO !! Digite um número !!')

        break

     
        
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

    arquivo.write(endereco.title() +':')# grava primeiras letras em maiúscula

    arquivo.write(num + ':')

    arquivo.write(resptec.title() +':')# grava primeiras letras em maiúscula

    arquivo.write(consanuall + ':')

    arquivo.write(medpotmensall + ':')

    arquivo.write(potinstall + '\n')

    arquivo.close()

    print()
   

def consulta_cadastro():

    arquivo = open('bancodedados.txt','r')
        
    arquivo.seek(0,0)

    lista = arquivo.readlines()       
         
    clientes = []

    for linha in lista:

        linha = linha[:-1] # remove o \n
        
        linha_split = linha.split(':')

        cliente = {'Nome':linha_split[0],'Endereco':linha_split[1],'Numero':linha_split[2],'resptec':linha_split[3],
                 'consanual':linha_split[4],'medpotmensal':linha_split[5],'potinstal':linha_split[5]}
        
        clientes += [cliente]

    print(clientes, end = '')

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

            print('Energia limpa !! Contribua com o planeta !!')

            print('Até o próximo projeto !!')

           
main()
    

          
          
