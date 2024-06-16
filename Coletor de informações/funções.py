def quantidade(lista, uf):
    cont = 0
    for i in range(len(lista)):
         dados = lista[i].split(',')
         if str(dados[2]) == uf:
            cont += 1
    return (cont)

def cidade(lista, cod):
    for i in range(len(lista)):
         dados = lista[i].split(',')
         if int(dados[0]) == cod:
            return dados[3]

def mesorregioes(lista, uf):
    misorreg = []
    for i in range (len(lista)):
         dados = lista[i].split(',')
         if dados[2] == uf:
             if dados[4] not in misorreg:
                misorreg.append(dados[4]) 
    return misorreg

def populacao(lista, uf):
    qtd = 0
    for i in range(len(lista)):
         dados = lista[i].split(',')
         if str(dados[2]) == uf:
            qtd += int(dados[17])
    return qtd

def latitude(lista, cod):
    for i in range(len(lista)):
         dados = lista[i].split(',')
         if float(dados[0]) == cod:
            return dados[13]

def longitude(lista, cod):
    for i in range(len(lista)):
         dados = lista[i].split(',')
         if float(dados[0]) == cod:
            return (dados[12])
         
