idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior = idade >= 18
crianca = idade < 12
adolecente = idade >= 12

if (maior):
    print("Você é maior de idade.")
else:
    if (crianca):
        print("Você é uma criança.")
    elif (adolecente):
        print("Você é um adolescente.")