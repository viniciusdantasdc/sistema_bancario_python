"""
Sistema Bancário
version 2.0
"""

from datetime import date 
from datetime import datetime as dt
from datetime import timedelta as td
import textwrap
#----------------------------------------------------------------------
data_brl_utf = date.today().strftime("%d/%m/%Y") # get date
# print(data_brl_utf)
today = dt.now() # get hours
# delta = td(days=3) # buscando o delta
hora_atual = (today).strftime("%H:%M:%S %A") # removendo delta aos dias

def menu():
  menu = """\n
      "Bem vindo ao BANCO CAPIXABA"
      [1]\tDepositar
      [2]\tSacar
      [3]\tExtrato
      [4]\tNova conta
      [5]\tNovo usuário
      [6]\tLista de contas
      [0]\tSair
  =>  """
  return input(textwrap.dedent(menu))
#----------------------------------------------------------------------
def depositar(saldo,valor,extrato, /): # arg por positional only
  
  if valor > 0:
    saldo += valor
    extrato += f"{dt.now()} Deposito:\tR$ {valor:.2f}\n"
    print("\n=== Depósito realizado com sucesso! ===")
  else:
    print("\n@@@ Operação falhou! Valor informado é inválido. @@@")

  return saldo, extrato

#----------------------------------------------------------------------
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):   # keyword only
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
  
    if excedeu_saldo:
      print("\n@@@ Operação falhou! Você nao tem saldo suficiente. motivo1 ")
    elif excedeu_limite:
      print("\n@@@ Operação falhou! Número máximo de saques excedidos. motivo2")

    elif excedeu_saques:
      print("\n@@@ Operação falhou! Número máximo de saques excedido. motivo3")

    elif valor > 0:
      saldo -= valor
      extrato += f"{dt.now()} Saque:\tR$ {valor:.2f}\n"
      numero_saques += 1
      print(f"\n=== Saque realizado com sucesso! ===")
    else:
      print("\n@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato
#----------------------------------------------------------------------
def exibir_extrato(saldo, /, *, extrato): # positional and keyword only
    print("EXTRATO".center(40,"="))
    print("Não houve movimentações em sua conta." if not extrato else extrato)
    print(f"\n\t\t\tSeu saldo é de\tR$ {saldo:.2f}")
    print("FIM".center(40,"="))
    
#----------------------------------------------------------------------
def criar_usuario(usuarios):
    
    cpf = input("Informe seu CPF (somente números): ")#tratar cpfs com inicio em 0
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
      print("\n?@@@ Já existe usuário com esse CPF! @@@")
      return
    
    nome = input("Seu nome: ")
    data_nascimento = input("Data de nascimento: ")
    endereco  = input("Endereço: ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,"cpf": cpf, "endereco": endereco})
    print("=== Usuário cadastrado com sucesso! ===")
#----------------------------------------------------------------------
def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] # encontrar o cpf indicado
  return usuarios_filtrados[0]  if usuarios_filtrados else None # conferer se há um único usuário, se não houver retorna NONE
#----------------------------------------------------------------------
def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("informe seu CPF de ususário: ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("\n=== Conta criada com sucesso! ===")
    return {"agencia": agencia, "numero_conta":numero_conta, "usuario":usuario}
  
  print("\n@@@ Usuário não encontrado, operação encerrada! @@@")
  # return None invisivel
#----------------------------------------------------------------------
def listar_contas(contas):
  for conta in contas:
    linha = f"""\
        Agência:\t{conta['agencia']}
        C\C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
    """
    print("=" *100)
    print(textwrap.dedent(linha))
#----------------------------------------------------------------------
def main():
  LIMITE_SAQUES = 3
  AGENCIA = "0001"

  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  usuarios = [] #{"Vinicius Dantas":10663828759}
  contas = []
  
  while True:
    opcao = menu()

    if opcao == "1":
        valor = float(input("inform o valor do depósito: "))
        saldo, extrato = depositar(saldo,valor,extrato)
    elif opcao == "2":
      valor = float(input("Informe o vlaor do saque: "))

      saldo, extrato = sacar(
        saldo=saldo,
        valor=valor,
        extrato=extrato,
        limite=limite,
        numero_saques=numero_saques,
        limite_saques=LIMITE_SAQUES,
      )
    elif opcao == "3":
      exibir_extrato(saldo, extrato=extrato)
    elif opcao == "4":
      criar_usuario(usuarios)
    elif opcao == "5":
      numero_conta = len(contas) + 1
      conta = criar_conta(AGENCIA, numero_conta, usuarios)
      if conta:
        contas.append(conta)
    elif opcao == "6":
      listar_contas(contas)
    elif opcao == "0":
      break
    else:
      print("Operação inválida, por favor selecione uma opção válida.")
main()