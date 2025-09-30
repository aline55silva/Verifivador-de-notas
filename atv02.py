#ATV01
def processar_pagamento():
    metodo_pagamento = input("Qual o método de pagamento escolhido (cartao/boleto)? ")

    if metodo_pagamento == "cartao":
        print("Processando pagamento no cartão...")
    elif metodo_pagamento == "boleto":
        print("Gerando boleto bancário...")
    else:
        print("Método de pagamento não reconhecido.")
processar_pagamento()

#ATV02
def classificar_idade(idade):
     if idade < 12:
      print("Criança")
     elif idade >13 and idade <=17:
      print("Adolescente")
     elif 18 <= idade <= 59:
      print("Adulto")
     elif idade >= 60:
      print("Idoso")
     else:
      print("Idade inválida")
classificar_idade(idade=int(input("Digite a idade: ")))


#ATV03
def classificar_entrega(entrega):
    if entrega == 'padrao':
        print("custa 10,00")
    elif entrega == 'expressa':
        print("custa 20,00")
    elif entrega == 'outra opcao':
        print("opcao de entrega diferente")
    else:
        print("opcao de entrega invalida")
classificar_entrega(entrega=input("Digite o tipo de entrega (padrao/expressa/outra opcao): ")) 
