# Dimensionamento de um sistema votofoltaico.

# Em função do consumo médio residencial, dimensionar a potência necessária (potência dos painéis)

# a ser instalada para atender a necessidade do consumo de energia.


class BD: # verifica se a função já foi criada. Caso, sim, não criará novamente.

    def cria_BD(cliente): # cria banco de dados

        arquivo = open('bancodedados.txt','w')

        arquivo.close()

def menuprincipal():

    print('='*40)

    print('     Dimensionamento sistema solar')

    print('='*40)

    print('='*40)

    op=0

    while (op!=3):


        print(' Escolha uma das opções.\n 1) Cadastrar projeto,\n 2) Consultar cadastro.\n 3) Sair')

        print('='*40)

        op = int(input('Opção:')) # Escolher opção

        if op == 1:

            cadastrar_projeto()

        elif op == 2:

            consulta_cadastro()

        elif op == 3:

            sair = int(input('Deseja realmente sair?\n1)Sim.\n2)Não.'))

            if sair == 1:

                print('Até o próximo projeto !!')

            else:
                op=0

        else:
            print("Insira uma opção válida\n")

                

def cadastrar_projeto():

        
    cliente = input('Nome do cliente: ')

    endereco = input('Endereço: ')

    numero = str(input('Número: '))

    resptec = input('Responsável técnico: ')

    consanual = float(input('Informe o consumo anual em (Kwh): '))

    consanual_str = str(consanual)# para usar no arquivo texto

    medpotmensal = consanual/12

    medpotmensal = round(medpotmensal,2) # arredonda 2 casas decimais

    medpotmensal_str = str(medpotmensal)# para usar no arquivo texto

    print('Média consumo mensal:',medpotmensal, 'Kwh.')

    potdia = medpotmensal/24

    potdia = round(potdia,2) # arredonda 2 casas decimais
     
        
    print('Média consumo diário:',potdia, 'Kwh.')

    hsolpleno = float(input('Informe as horas de sol pleno: '))

    potinstal = potdia/hsolpleno

    potinstal = round (potinstal,2) # arredonda 2 casas decimais

    potinstal_str = str(potinstal)# para usar no arquivo texto

          
    print('Potência a ser instalada:',potinstal, 'Kwp.')

    print()

    arquivo = open('bancodedados.txt','a')

    arquivo.write(cliente.title() +':') # grava primeiras letras em maiúscula

    arquivo.write(endereco.title() +':')

    arquivo.write(numero + ':')

    arquivo.write(resptec.title() +':')

    arquivo.write(consanual_str + ':')

    arquivo.write(medpotmensal_str + ':')

    arquivo.write(potinstal_str + '\n')

    arquivo.close()

    print()  
    

def consulta_cadastro():

    arquivo = open ('bancodedados.txt','r').readlines()

    while (opcao!=3):

        opcao = int(input('Que tipo de consulta deseja fazer?\n1) Completa.\n2) Unica.\n3)Sair\n'))

        if (opcao == 1):

            arquivo = [str(x).rstrip() for x in arquivo] # "srt(x)" converte valores dentro do arquivo em valores exatos. "rstrip" remove espaços entre as linhas

            for linha in arquivo:

                print(linha)

            print()
    
        elif (opcao == 2):

            nome= input("Digite o nome do cliente: ")

            nome_achado= False

            for cliente in arquivo:

                if (cliente[-1]=="\n"):
                    
                    cliente= cliente[:-1]

                else:

                    cliente_info= cliente.split(":")

                    cliente_nome= cliente_info[0]

                    if (cliente_nome==nome):

                        nome_achado= True

                        dict_cliente={"Cliente": cliente_info[0],
                                      "Endereço": cliente_info[1],
                                      "Número": int(cliente_info[2]),
                                      "Responsável Técnico": cliente_info[3],
                                      "Consumo Anual": cliente_info[4],
                                      "Potência média mensal": cliente_info[5],
                                      "Potência Instalada": cliente_info[6]
                                      }
                         
                        print dict_cliente

            if (not nome_achado):

                print("Cliente não cadastrado\n")

            

        elif (opcao ==3):

        else:
            print("Opção inválida\n")
            


def main():

    menuprincipal()
        
    print()

      

main()
    
