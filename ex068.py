#068 Faça um programa que jogue par ou ímpar com o computador. O jogo só será
# interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.
from random import randint
v = 0
while True:
    jogador = int(input(" Diga um valor: "))
    comutador = randint(0, 11)
    total = jogador + comutador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input(" Par ou Ímpar? [P/I] ")).strip().upper()[0]
    print(f" Você jogou {jogador} e o computador jogou {comutador}. Total de {total}", end="")
    print(" DEU PAR " if total % 2 == 0 else " DEU ÍMPAR ")
    if tipo == "P":
        if total % 2 == 0:
            print("Você VENCEU! ")
            v = v + 1
        else:
            print(" Você PERDEU! ")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("VocÊ VENCEU! ")
            v = v + 1
        else:
            print("Você PERDEU! ")
            break
    print("Vamos jogar novamente...")
print(f"Você venceu {v} vezes - PARABÉNS ")
