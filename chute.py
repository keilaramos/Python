chute = input("Digite seu chute:")
chute = int(chute)
acertou = chute == 14
maior = chute > 14
menor = chute < 14

if (acertou):
    print("Parabéns você acertou!")
elif(maior):
    print("Seu chute está errado e é maior que o valor correto!")
else:
    print("Seu chute está errado e é menor que o valor correto!")