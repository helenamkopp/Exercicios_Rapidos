from time import sleep
num = int(input("Digite um número para saber sua tabuada: "))
for c in range(1, 11):
    sleep(0.5)
    print("{} x {:2} = {} ".format(num, c, num*c))