# No maximo 3 saques
# Limite maximo saque: 500
# Se nao tiver saldo em conta, retornar mensagem informando falta de saldo
# Retornar extrato no formato R$ xxxx.xx

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

operacoes = []
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)

  if opcao == "d":
    deposito = float(input("Insira o valor deseja depositar: "))
    if float(deposito) <= 0:
      print("O valor a ser depositado precisa ser positivo:")
    else:
      print(f"Valor depositado de R$ {deposito:.2f} com sucesso!")
      saldo += deposito 
      operacoes.append(f"Deposito: R$ {deposito:.2f}")

  elif opcao == "s":
    saque = float(input("Insira o valor deseja sacar: "))
    if float(saque) > 500:
      print("O valor maximo de saque e R$500")
    elif float(saque) <= 0:
      print("O valor a ser sacado precisa ser maior que zero")
    elif float(saque) > saldo:
      print("Saldo insuficiente")
    else:
      numero_saques += 1
      if numero_saques > LIMITE_SAQUES:
        print("Nao foi possivel realizar essa operacao. Limite de saques diarios atingidos!")
      else:
        print(f"saque no valor de {saque:.2f} realizado com sucesso")
        saldo -= saque
        operacoes.append(f"Saque: R$ {saque:.2f}")

  elif opcao == "e":
    if operacoes == []:
      print("========== EXTRATO ==========\n")
      print("Nao houveram movimentacoes\n")
      print("Saldo: R$ 0.00 \n")
      print("=============================")
    else:
      print("========== EXTRATO ==========\n")
      for operacao in operacoes:
        print(operacao)
      print(f"\nSaldo: R$ {saldo:.2f}\n")
      print("=============================")
  
  elif opcao == "q":
    break
  
  else:
    print("Operacao invalida, por favor selecione novamente a operacao desejada")