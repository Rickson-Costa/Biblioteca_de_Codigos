import funções

nome_do_cliente = ["Raul", "Cristiano", "Francisco", "Lucas  "]
valor_da_compra = [500, 400, 200, 1000]
tipo_de_pagamento = [1,2,2,1]

print(funções.media(valor_da_compra))
print(funções.maior(valor_da_compra))
print(funções.total(valor_da_compra))
for i in range (len(nome_do_cliente)):
    print(funções.senha(nome_do_cliente[i]))
print(funções.menor(valor_da_compra))