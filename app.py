from flask import Flask, render_template, request, jsonify
import os
from firebase_admin import credentials, firestore, initialize_app
from flask import redirect, url_for


app=Flask(__name__)
cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
initialize_app(cred)
firestore_db = firestore.client()


@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        data = request.form.to_dict()  # Converte os dados do formulário para um dicionário
        doc_ref = firestore_db.collection('Relatório de serviço').document()
        doc_ref.set(data)  # Salva os dados do formulário no Firestore
        totalPoliciais = data.get('totalPoliciais')
        return jsonify({'redirect': 'alguma_rota.html', 'totalPoliciais': totalPoliciais})
    except Exception as e:
        app.logger.error("Erro ao salvar no Firestore: %s", e)
        return jsonify({'error': 'Erro ao processar o formulário'}), 500
    
    
@app.route('/salvar_detalhes_da_guarnicao', methods=['POST'])
def salvar_detalhes():
    try:
        doc_ref = firestore_db.collection('Relatório de serviço')
        data = request.form.to_dict()
        doc_ref.set(data)
        # Retorna uma resposta de sucesso
        return jsonify({'success': 'Detalhes da guarnição salvos com sucesso.'})
    except Exception as e:
        app.logger.error("Erro ao salvar detalhes da guarnição no Firestore: %s", e)
        return jsonify({'error': 'Erro ao processar o formulário de detalhes da guarnição'}), 500
    
@app.route('/alguma_rota', methods=['GET', 'POST'])
def alguma_funcao():
    try:
        doc_ref = firestore_db.collection('Relatório de serviço')
        data = request.form.to_dict()
        doc_ref.set(data)
        # Retorna uma resposta de sucesso
        return jsonify({'success': 'Detalhes da guarnição salvos com sucesso.'})
    except Exception as e:
        app.logger.error("Erro ao salvar detalhes da guarnição no Firestore: %s", e)
        return jsonify({'error': 'Erro ao processar o formulário de detalhes da guarnição'}), 500
    pass



if __name__ == '__main__':
    app.run(debug=True)
