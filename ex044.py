#Desconto com juros, conforme escolha da forma de pagamento.

print("{:=^40}".format(" LOJAS HELENA "))
preço = float(input("Digite o preço das compras R$ "))
print('''Formas de pagamento:
[1] À VISTA - NO DINHEIRO OU CHEQUE
[2] À VISTA - NO CARTÃO
[3] 2 X NO CARTÃO
[4] 3 X OU + NO CARTÃO
''')
opção = int(input("Qual é a sua opção? "))
if opção == 1:
    total = preço - (preço * 10) / 100
elif opção == 2:
    total = preço - (preço * 5) / 100
elif opção == 3:
    total = preço
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R$ {:.2f} - SEM JUROS ".format(parcela))
elif opção == 4:
    total = preço + (preço * 20) / 100
    totalparc = int(input("Quantas parcelas? "))
    parcela = total / totalparc
    print("Sua compra será parcelada em {}x de R$ {:.2f} - COM JUROS ".format(totalparc, parcela))
else:
    total = preço
    print("OPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente!")
print(" Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final".format(preço, total))
