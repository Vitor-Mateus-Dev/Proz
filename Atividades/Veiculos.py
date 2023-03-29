"""Desenvolva um código que utilize as seguintes características de um veículo:
- Quantidade de rodas;
- Peso bruto em quilogramas;
- Quantidade de pessoas no veículo.

Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
A: Veículos com duas ou três rodas;
B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; E: Veículos com quatro rodas ou mais e com mais de 6000 kg."""

#verificar as informações do veiculo
rodas = int(input("Informe a quantidade de rodas do veículo: "))
peso = float(input("Informe o peso bruto do veículo em quilogramas: "))
pessoas = int(input("Informe a quantidade de pessoas no veículo: "))

#tomada de  decisões
if rodas <= 3:
    print ("Seu veiculo é do tipo A")
elif rodas == 4 and pessoas <= 8:
    print ("seu veiculo é do tipo B")
elif rodas >= 4 and peso >= 3500 and peso <= 6000:
    print ("seu veiculo é do tipo C")
elif rodas >= 4 and pessoas >= 8:
    print("seu veiculo é do tipo D")
elif rodas >= 4 and peso > 6000: 
    print ("seu veiculo é do tipo E")
else:
    print ("informações invalidas")