from time import sleep
fichaanualalunos = list()
cont = 0
maiormedia = 0
menormedia = 0
maioraluno = " "
menoraluno = " "
alunoap = 0
alunoex = 0
status = " "
print("-.-" * 15)
print("   QUADRO DE STATUS DOS ALUNOS:  ")
print("-.-" * 15)
while True:
    nome = str(input("Aluno: "))
    cont = cont + 1
    n1 = float(input("N1: "))
    n2 = float(input("N2: "))
    n3 = float(input("N3: "))
    n4 = float(input("N4: "))
    ma = (n1 + n2 + n3 + n4) / 4
    if cont == 1:
        maioraluno = nome
        maiormedia = ma
    elif ma > maiormedia:
        maioraluno = nome
        maiormedia = ma
    if cont == 1:
        menoraluno = nome
        menormedia = ma
    elif ma < menormedia:
        menoraluno = nome
        menormedia = ma
    if ma >= 7.0:
        status = ("APROVADO")
        alunoap = alunoap + 1
    else:
        status = ("EXAME")
        alunoex = alunoex + 1
    fichaanualalunos.append([nome, n1, n2, n3, n4, ma, status])
    addaluno = " "
    while addaluno not in "SN":
        addaluno = str(input("ADICIONAR ALUNO? [S/N]: ")).strip().upper()[0]
    if addaluno == "N":
        break
    print("- -" * 20)
print("AGUARDE.. PROCESSANDO DADOS")
sleep(1)
print("-" * 50)
print(f"{'Nº':<4}{'NOME':<10}{'N1':<5}{'N2':<5}{'N3':<5}{'N4':<5}{'MA':>5}{'STATUS':>10}")
print("-" * 50)
# para cada indice nos nomes dos alunos
for i, n in enumerate(fichaanualalunos):
    print(f"{i:<4}{n[0]:<10}{n[1]:<5.1f}{n[2]:<5.1f}{n[3]:<5.1f}{n[4]:<5.1f}{n[5]:>5.1f}{n[6]:>10}")
print()
print("-" * 50)
print()
print("-" * 30)
print(f"ALUNOS APROVADOS: {alunoap} ")
print(f"ALUNOS EM EXAME: {alunoex} ")
print("-" * 30)
print(f"MAIOR MÉDIA ANUAL: {maioraluno} - {maiormedia:.1f}")
print(f"MENOR MÉDIA ANUAL: {menoraluno} - {menormedia:.1f}")
print("-" * 30)
print("PROGRAMA FINALIZADO")
