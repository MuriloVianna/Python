import random

print("\n\nJogo do acerte o número\n")
numero_teto = input("Para começar digite um número máximo por favor!!\n")

if numero_teto.isdigit():
    numero_teto = int(numero_teto)
else: 
    print("Erro: Favor informar um número!")
    quit()

random_numero = random.randint(0, numero_teto)

tentativas = 0

while True:
    resposta = input("Adivinhe o número: ")

    if resposta.isdigit():
        resposta = int(resposta)
    else:
        print("Erro: Informe um número")
        continue

    tentativas = tentativas + 1

    if resposta == random_numero: 
        print("Acertou!")
        break
    elif resposta > random_numero:
        print("Chutou alto, o número é menor que esse...\n")
    else:
        print("Chutou baixo, o número é maior que esse...\n")

print("\nNº de tentativas: " + str(tentativas))