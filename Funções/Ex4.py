def voto(nascimento):
    idade = 2023 - nascimento
    if idade < 16:
        print(f"Sua idade é {idade}, portanto o voto é negado")
    if idade >= 16 and idade < 18:
        print(f"Sua idade é {idade}, portanto o voto é opcional")
    else:
        print(f"Sua idade é {idade}, portanto o voto é obrigatório")


nascimento = int(input("Digite seu ano de nascimento: "))
voto(nascimento)