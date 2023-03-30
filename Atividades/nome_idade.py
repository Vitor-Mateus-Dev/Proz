# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
# Resposta:
while True:
    nome = str(input("digite seu nome"))
    nasceu = int(input("digite o ano que voce nasceu"))
    if nasceu >= 1922 and nasceu <= 2021:
            idade = 2022 - nasceu
            print(nome, idade)
            break

    else:
            print(
                "ano de nascimento deve ser maior que 1922 e menor que 2021, tente de novo")
