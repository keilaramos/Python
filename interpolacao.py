print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")
numero_secreto = 14
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu número: ")
    print("Você digitou " , chute_str)

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!")
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")

    rodada = rodada + 1
#Interpolação de números e data
print("Fim do jogo")
print("Interpolação de números e data")
print("R$ {:6.1f}".format(1400.14))
print("R$ {:07.2f}".format(1.396))
print("Data {:02d}/{:02d}".format(26,10))
nome = 'Keila'
print(f'Meu nome é {nome}')
print("Elaborado pela  Sra. {1} {0}".format("Ramos","Keila"))
