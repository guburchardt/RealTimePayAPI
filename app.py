from flask import Flask, jsonify, request
from repository.database import db
from db_models.payment import Payment
from datetime import datetime, timedelta


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'


db.init_app(app)

@app.route('/payments/pix', methods=['POST']) #Criacao de pagamento
def create_payment_pix():
    data = request.get_json()
    
    # Validações
    if 'value' not in data:
        return jsonify({"message": "Invalid Value"}), 400

    expiration_date = datetime.now() + timedelta(minutes=30) # Pega data atual e soma mais 30 minutos

    new_payment = Payment(value=data['value'], expiration_date=expiration_date)
    
    db.session.add(new_payment)
    db.session.commit()

    return jsonify({
        "message": "The payment has been created",
        "payment": new_payment.to_dict()
    })

@app.route('/payments/confirmation', methods=['POST']) #Webhook - Confirmacao de um pagamento existente
def pix_confirmation():
    return jsonify({"message": "The payment has been confirmed"})

@app.route('/payments/pix/<int:payment_id>', methods=['GET']) #Visualizacao de um pagamento existente
def payment_pix_page(payment_id):
    return 'pagamento pix'

if __name__ == '__main__':
    app.run(debug=True)
