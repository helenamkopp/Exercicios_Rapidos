dadoscolaboradores = list()
maisquinhentos = 0
menosquinhentos = 0
cont = 0
nomemaior = " "
nomemenor = " "
maiorsalario = 0
menorsalario = 0
from time import sleep
while True:
    colaborador = str(input("Nome: "))
    cont = cont + 1
    cargo = str(input("Cargo: "))
    salario = float(input("Salário: "))
    if salario <= 1000.00:
        aumentos = salario + (salario * 10)/100
    elif salario <= 2500.00:
        aumentos = salario + (salario * 5)/100
    else:
        aumentos = salario + (salario * 2)/100
    valoraumentos = aumentos - salario
    if cont == 1:
        maiorsalario = aumentos
        nomemaior = colaborador
    elif aumentos > maiorsalario:
        maiorsalario = aumentos
        nomemaior = colaborador
    if cont == 1:
        menorsalario = aumentos
        nomemenor = colaborador
    elif aumentos < menorsalario:
        menorsalario = aumentos
        nomemenor = colaborador
    if valoraumentos >= 500.00:
        maisquinhentos = maisquinhentos + 1
    else:
        menosquinhentos = menosquinhentos + 1
    dadoscolaboradores.append([colaborador, cargo, salario, aumentos, valoraumentos])
    addcolaborador = " "
    while addcolaborador not in "SN":
        addcolaborador = str(input("Novo colaborador? [S/N]: ")).strip().upper()[0]
    if addcolaborador == "N":
        break
print()
print("-" * 50)
print("PROCESSANDO DADOS.. ")
sleep(0.8)
print("-.-" * 30)
print(f"{'Nº':<4}{'NOME':<12}{'CARGO':<14}{'SALÁRIO':<15}{'NOVO SALÁRIO':<15}{'VALOR AUMENTO':<15}")
for i, c in enumerate(dadoscolaboradores):
    print(f'{i:<4}{c[0]:<12}{c[1]:<14}R${c[2]:<15.2f}R${c[3]:<15.2f}R${c[4]:<15.2f}')
print()
print("- -" * 30)
print(f"{maisquinhentos} COLABORADORES RECEBERAM MAIS DE R$ 500,00 EM AUMENTO SALARIAL. ")
print(f"{menosquinhentos} COLABORADORES RECEBERAM MENOS DE R$ 500,00 EM AUMENTO SALARIAL. ")
print()
print(" - -" * 30)
print(f"MAIOR SALÁRIO: R$ {maiorsalario} - {nomemaior}")
print(f"MENOR SALÁRIO: R$ {menorsalario} - {nomemenor}")
print()
print("FIM DE ANÁLISE.")