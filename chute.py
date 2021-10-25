print("*********************************")
print("Bem vindo ao jogo do chute!")
print("*********************************")

numero_secreto = 14
chute = input("Digite seu chute:")
print("Você digitou " , chute)
chute = int(chute)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Parabéns você acertou!")
elif(maior):
    print("Seu chute é Maior que o número secreto!")
else:
    print("Seu chute é menor que o número secreto!")
    print("Fim do jogo")
