import uuid # Gerador de identificador aleatório
import qrcode

class Pix:
    def __init__(self):
        pass
    
    def create_payment(self):
        # Criar o pagamento na instituição financeira
        bank_payment_id = uuid.uuid4()

        #create code
        hash_payment = f'hash_payment_{bank_payment_id}'

        # qr code
        img = qrcode.make(hash_payment)

        # save image as png file
        img.save(f"static/img/qr_code_payment_{bank_payment_id}.png")


        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path": f"static/img/qr_code_payment_{bank_payment_id}."
        }
