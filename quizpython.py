print("\n\nBem vindo ao Quiz de Python!!!")
comecar = input("Vamos começar? (S/N)\n") 

if comecar != "S" and comecar != "s":   #"and" usado para para caso o usuario use letra maiuscula ou minuscula
    quit()                              #função quit() que encerra a leitura do script

pontos = 0

print("\nComeçando...")
print("\n1-) Para incrementar na variavel 'a=0', o melhor atalho é: \n\nA) a += 1\nB) a = a + 1\nC) a++")
resposta_1 = input("\nResposta: ")

if resposta_1.lower() == "a":           #função lower() para deixar a string em letra minuscula
    print("Correto!\n\n")
    pontos = pontos + 1
else:
    print("Incorreto!\n\n")

print("2-) Para imprimir algo na tela em Python o comando correto a ser usado é: \n\nA) cout\nB) print\nC) printf")
resposta_2 = input("\nResposta: ")

if resposta_2.lower() == "b":
    print("Correto!\n\n")
    pontos = pontos + 1
else:
    print("Incorreto!\n\n")

print("3-) O comando para receber a entrada do usuario em Python é: \n\nA) cin\nB) scanf\nC) input")
resposta_3 = input("\nResposta: ")

if resposta_3.lower() == "c":
    print("Correto!\n\n")
    pontos = pontos + 1
else:
    print("Incorreto!\n\n")

print(f"O quiz acabou!\nPontuação: {pontos}/3")   #fstring: possibilita escrever valores de variaveis 