"""
Sistema Bancário
version - 1.0
"""

from datetime import date 
from datetime import datetime as dt
from datetime import timedelta as td
#----------------------------------------------------------------------
data_brl_utf = date.today().strftime("%d/%m/%Y") # get date
# print(data_brl_utf)
today = dt.now() # get hours
# delta = td(days=3) # buscando o delta
hora_atual = (today).strftime("%H:%M:%S %A") # removendo delta aos dias

# print(hora_atual)
# =>> SETAR AS 24H DO DIA PARA LIMITAR OS 3 SAQUES DENTRO DESTE TIME
#----------------------------------------------------------------------
# lista_clientes = ['Vinicius Dantas', 'Patricia Forequi']
cliente = "Vinicius Dantas"
#----------------------------------------------------------------------

menu = f"""
    {data_brl_utf} {hora_atual}
    Bom dia! Sr(a). {cliente} 
    Bem vindo ao BANCO CAPIXABA 
    Escolha uma das opções:
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [0] - Sair
=>  """

msgExtrato = "EXTRATO"


saldo = 0
# dep_trackRec = []
# saq_trackRec = []
limite = 500
extrato = "" #[]
numero_Saques = 0
LIMITE_SAQUES = 3

while True:  
  opcao = int(input(menu + 'Opção '))

  if opcao == 1:
    depositos_em_conta = int(input("Informe o valor de deposito: "))

    if depositos_em_conta > 0:
      saldo += depositos_em_conta
      # extrato.append(f"""{dt.now()} Depositado R$ {depositos_em_conta:.2f}""")
      extrato += f"{dt.now()} Depositado R$ {depositos_em_conta:.2f}\n"
    else:
      print("Valor informado é inválido")
       
  elif opcao == 2:
    if numero_Saques < LIMITE_SAQUES:
      saque_em_conta = int(input("Informe o valor de saque: "))
      if saque_em_conta <= limite:
        saldo -= saque_em_conta
        # extrato.append(f"""{dt.now()} Sacado R$ {saque_em_conta:.2f}""")
        extrato += f"{dt.now()} Sacado R$ {saque_em_conta:.2f}\n"
        numero_Saques += 1
      elif saque_em_conta >= limite:
        print(f"""Saque excedente ao limite diário de R$ {limite:.2f}""")
      else:
        print("Limite de saque excedido!")
    else:
      print("Número de saques excedente no dia!")


  elif opcao == 3:
    print(msgExtrato.center(40,"="))
    print("Não houve movimentações em sua conta." if not extrato else extrato)
    print(f"""
    Seu saldo é de R$ {saldo:.2f}
          
    """
    )

  elif opcao == 0:
    break

  else:
    print("Operação inválida, por favor selecione uma opção válida.")