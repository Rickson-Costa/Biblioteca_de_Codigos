# Esse é um codigo simples que tem como objetivo, substituir palavras-chaves dentro de um documento word, por palavras inseridas pelo sistema.

from docx import Document
from datetime import datetime

arquivo = "Oficio modelo.docx"
documento = Document(arquivo)
contador = 1

while True:
    contador += 1

    nome = "Fulano da Silva" # Ou puxar de algum lugar
    cargo = "Analista"
    empresa = "GIT HUB"

    # Atualiza a data em tempo real
    dia = str(datetime.now().day)
    mês = str(datetime.now().month)
    ano = str(datetime.now().year)

    # Dicionario de subtituição
    referencias = {
        "Nome da Pessoa" : nome,
        "Cargo" : cargo,
        "Órgão" : empresa,
        "05" : dia,
        "dezembro" : mês,
        "2023" : ano,   
        "------" : contador,
        'Descrever, de forma sucinta, o conteúdo do documento___' : "MENSAGEM DO COMENTO",
        }

    # Códgio de Substituição
    for paragrafo in documento.paragraphs:
        for codigo in referencias:
            valor = referencias[codigo]
            paragrafo.text = paragrafo.text.replace(codigo, str(valor))
    documento.save(f"Documento de {nome} - N° {contador}.docx")

    break