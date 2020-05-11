import random
nomes = list()
pessoa = list()
print("-=" * 25)
print("SORTEADOR DE NOMES")
print("-=" * 25)
while True:
    pessoa = str(input("Nome: "))
    nomes.append(pessoa[:])
    addpessoa = " "
    while addpessoa not in "SN":
        addpessoa = str(input("Adicionar uma pessoa? [S/N] ")).strip().upper()[0]
    if addpessoa == "N":
        break
    print("- " * 20)
quant = int(input("Quantos nomes você quer que eu sorteie?! "))
escolha = random.sample(nomes, quant)
print(escolha)
print("FIM DO PROGRAMA ")