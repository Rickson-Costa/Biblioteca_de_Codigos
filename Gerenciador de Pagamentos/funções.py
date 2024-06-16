def desconto(valor, tipo):
    if valor >= 0 and valor <= 100:
        if tipo == 1:
            return 5
        else:
            return 3
    elif valor > 100 and valor <= 200:
        if tipo == 1:
            return 10
        else: 
            return 6
    elif valor > 200 and valor <= 400:
        if tipo == 1:
            return 15
        else:
            return 12
    else:
        if tipo == 1:
            return 20
        else:
            return 15
        
def cupons(valor):
    if valor >= 0 and valor <= 100:
        return 2
    
    elif valor > 100 and valor <= 200:
       return 4
    
    elif valor > 200 and valor <= 400:
        return 6
    
    else:
        return 8

def media(lista):
    media = 0
    for i in range (len(lista)):
        media += lista[i]
    media = media/(len(lista))
    return media

def maior(lista):
    maior = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior

def total(lista):
    soma = 0
    for i in range(len(lista)):
        soma += cupons(lista[i])
    return soma
        
def senha(nome):
    senha = nome.upper()
    senha = senha[:3]
    return senha

def menor(lista):
    menor = 1000000000
    for i in range(len(lista)):
        if menor > lista[i]:
            menor = lista[i]
    return menor

def pagamento(lista):
    contador1 = 0
    contador2= 0
    for i in range(len(lista)):
        if lista[i] == 1:
            contador1 += 1
        else:
            contador2 += 1
