def maior(valores):
    maiorvalor = 0
    for i in valores:
        if i > maiorvalor:
            maiorvalor = i
    print(f"O maior valor é: {maiorvalor}")


lista = []
escolha = int(input("Digite quantos valores você quer: "))
for i in range(escolha):
    pergunta = int(input("Informe o valor: "))
    lista.append(pergunta)
maior(lista)
