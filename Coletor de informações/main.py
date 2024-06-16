import funções

arq = open("Dados.txt", 'r', encoding="utf8" )
registros = arq.read().splitlines()
arq.close()

uf = "PB"
cod_da_cidade = 1100015

print(funções.quantidade(registros, uf))
print(funções.cidade(registros, cod_da_cidade))
print(funções.mesorregioes(registros, uf))
print(funções.populacao(registros, uf))
print(funções.latitude(registros, cod_da_cidade))
print(funções.longitude(registros, cod_da_cidade))