def calcular_media():
    valores = []
    
    while True:
        valor = int(input("Digite um valor inteiro positivo (ou um valor negativo para terminar): "))
        if valor < 0:
            break
        valores.append(valor)
    
    if len(valores) == 0:
        return 0
    
    media = sum(valores) / len(valores)
    return media