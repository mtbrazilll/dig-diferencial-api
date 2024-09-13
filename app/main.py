from flask import Flask, request, jsonify

# Inicializa a aplicação Flask
app = Flask(__name__)

# Rota básica para verificar se o servidor está funcionando
@app.route("/")
def hello_world():
    return "Hello, World!"

# Simulação de processamento de IA
def ia_processing(input_data):
    # Aqui seria onde o processamento de IA ocorre
    # Exemplo simples: transforma o texto recebido em maiúsculas
    processed_data = input_data.upper()
    return processed_data

# Rota para o serviço de IA que recebe dados via POST
@app.route('/api/ia_service', methods=['POST'])
def ia_service():
    try:
        # Recebe o JSON do request
        data = request.get_json()

        # Acessa um campo específico do JSON (ajuste conforme necessário)
        input_text = data.get('input_text', '')

        # Processa os dados recebidos pela função de IA
        result = ia_processing(input_text)

        # Retorna a resposta no formato JSON
        response = {
            'processed_text': result,
            'status': 'success'
        }
        return jsonify(response), 200

    except Exception as e:
        # Em caso de erro, retorna uma mensagem de erro
        return jsonify({'error': str(e)}), 400

# Executa a aplicação Flask e define uma porta específica (por exemplo, porta 5001)
if __name__ == '__main__':
    app.run(debug=True, port=5000)
