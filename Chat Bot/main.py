from flask import Flask, render_template, request
import openai, os, openpyxl

app = Flask(__name__)

senha_file = "senha.txt"
org_file = "org.txt"

app.config['TEMPLATES_AUTO_RELOAD'] = True

with open(senha_file, 'r') as senha_file:
    api_key = senha_file.read()

with open(org_file, 'r') as org_file:
    organization_key = org_file.read()

openai.organization = os.getenv('OPENAI_ORG', organization_key)
openai.api_key = os.getenv('OPENAI_API_KEY', api_key)


def chatbot_logic(user_input, planilha):
    data = []

    # Verificar se a entrada do usuário está no arquivo Excel
    for row in planilha.iter_rows(min_row=1, max_row=planilha.max_row, min_col=1, max_col=2):
        if user_input in row[0].value:
            data = f"Pergunta: {row[0].value} Resposta: {row[1].value}"
            return data

    # Se não encontrado, fazer uma chamada à API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eu sou um Chatobot do Hospital Napoleão."},
                {"role": "user", "content": user_input},
            ]
        )
        data = response['choices'][0]['message']['content']

        # Encontrar a primeira linha vazia e escrever no arquivo Excel
        linha_vazia = planilha.max_row + 1
        planilha.cell(row=linha_vazia, column=1, value=user_input)
        planilha.cell(row=linha_vazia, column=2, value=data)

        # Salvar as alterações no arquivo Excel
        planilha.parent.save('banco.xlsx')

    except Exception as e:
        print(f"Erro: {e}")

    return data


@app.route('/')
def home():
    return render_template("inicio.html")


@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot_route():
    data = []
    if request.method == 'POST':
        user_input = request.form.get('P1')
        arquivo = openpyxl.load_workbook('banco.xlsx')
        planilha = arquivo.active
        data = chatbot_logic(user_input, planilha)

    return render_template("chatbot.html", data=data)


@app.route('/consultar.ramal', methods=['GET', 'POST'])
def consultar_setor():
    resposta = None
    ramal = None
    if request.method == 'POST':
        try:
            arquivo = openpyxl.load_workbook('ramais.xlsx')
            sheet = arquivo.active
            pergunta = request.form['PR1'].upper()

            if pergunta != "PARE":
                for row in sheet.iter_rows(min_row=1, max_row=sheet.max_row, min_col=1, max_col=3):
                    if pergunta in str(row[0].value):
                        ramal = str(row[0].value)
                        resposta = f"O número do ramal é: {row[1].value} e fica no setor {row[2].value}"
        except KeyError:
            print("KeyError: 'PR1' not found in request.form")

    return render_template("chatramal.html", resposta=resposta, ramal=ramal)


if __name__ == '__main__':
    app.run(debug=True)
