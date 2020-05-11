# 054 - Crie um programa que leia o ano de nascimento de 7 pessoas
# no final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1, 8):
    nasc = int(input("Em que ano a {} pessoa nasceu? ".format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior = totmaior + 1
    else:
       totmenor = totmenor + 1
print("Ao todo tivemos {} pessoas maiores de idade".format(totmaior))
print("E ao todo tivemos {} pessoas menores de idade".format(totmenor))

# o tot maior começa no 0 - porque não tem nenhuma pessoa ainda e depois soma quantos tiverem.