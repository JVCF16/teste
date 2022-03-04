#=================================================================================================================================================#
# Import
from datetime import date

#=================================================================================================================================================#
# Função - Etapas 1 e 2

def obter_limite():
    
    nome = input('\nQual é o seu nome? ')

    print ('\nOlá, {} seja bem-vindo(a) à Loja Helix! Meu nome é João Victor Carvalho Fonseca.'.format(nome))
    print ('\n1. Para estabelecer o seu limite de compras, necessito obter algumas informações para realizar sua análise de crédito. Por favor, informe:')

  
    data_Atual = date.today()
    ano_Atual = data_Atual.year    
    cargo = input ('\n   a. Qual é seu cargo na empresa em que trabalha atualmente? ')
    salario = float(input('   b. Qual é seu salário? R$ '))
    ano_De_Nascimento = int(input('   c. Qual é seu ano de nascimento? '))
    idade = ano_Atual - ano_De_Nascimento
    limite_De_Gasto = salario*(idade / 1000)+ 100


    print ('\n\n   Dados informados:')
    print ('\n   - Cargo:',cargo)
    print ('   - Salário: R$ {:.2f}'.format(salario))
    print ('   - Ano de nascimento:',ano_De_Nascimento)
    print ('   - Sua idade aproximada é:',idade)
    print ('\n\n   De acordo com os dados, seu limite de gasto disponível para compra é: R${:.2f}'.format(limite_De_Gasto))

    return limite_De_Gasto, idade, salario


#=================================================================================================================================================#
limite, idade, salario = obter_limite() 

saldo_Restante = limite

        
#=================================================================================================================================================#
# Função - Etapa 3 #


def verificar_produto(limite, idade):
    
    global saldo_Restante
    produto = str(input('\n   a. Digite o nome do produto: '))
    preço_Do_Produto = float(input ('   b. Digite o preço: R$ '))
    preço_Do_Produto_Com_Desconto = preço_Do_Produto*(96/100)

    # Primeira estrutura condicional
    if preço_Do_Produto <= (limite * 0.6):
        print ('      |Liberado!|')
    elif (limite * 0.6) <= preço_Do_Produto <= (limite * 0.9):
        print ('      |Liberado ao parcelar em até 2 vezes.|')
    elif (limite * 0.9) <= preço_Do_Produto <= (limite * 1):
        print ('      |Liberado ao parcelar em 3 ou mais vezes.|')
    else: 
        print ('      |Bloqueado|')
        print ('\n     Seu saldo é insuficiente. Para fazer uma nova compra, reinicie o programa.')
        exit()
                
    # Segunda estrutura condicional        
    if  28 <= preço_Do_Produto <= idade:
        print ('\nVocê receberá um desconto em seu produto. O preço com o desconto aplicado, é: R${:.2f}'.format(preço_Do_Produto_Com_Desconto))
        saldo_Restante -= preço_Do_Produto_Com_Desconto
        print('\n      Saldo Restante: R${:.2f}'.format(saldo_Restante))    
    else:  
        saldo_Restante -= preço_Do_Produto
        print('\n      Saldo Restante: R${:.2f}'.format(saldo_Restante))
       
        
# Global        
n = int(input('\n\n2. Quantos produtos você deseja cadastrar? '))

saldo_Restante = limite

for n in range(n):
    verificar_produto(limite, idade)
print('\n\n      Obrigado, até a próxima!')


# Aluno: João Victor Carvalho Fonseca - Módulo 1 - ADS - 04/2020

