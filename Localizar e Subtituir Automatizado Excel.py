import pandas as pd

# Carrega a planilha de origem
origem = pd.read_excel('Origem.xlsx')

# Carrega a planilha de destino
destino = pd.read_excel('Destino.xlsx')

# Contador 
cont = 0

# Itera sobre os códigos da planilha de destino
for index, row in destino.iterrows():
    codigo = row['Codigo']
    
    # Verifica se o código existe na planilha de origem
    if codigo in origem['Codigo'].values:
        # Obtém o valor correspondente na planilha de origem
        valor = origem.loc[origem['Codigo'] == codigo, 'Valor'].iloc[0]
        
        # Insere o valor na planilha de destino
        destino.at[index, 'Valor'] = valor
        
        print(f'Alterei {cont}')
        cont += 1

# Salva a planilha de destino atualizada
destino.to_excel('Destino.xlsx', index=False)

print("Processo concluído com sucesso!")
