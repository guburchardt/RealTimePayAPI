import uuid # Gerador de identificador aleatório
import qrcode

class Pix:
    def __init__(self):
        pass
    
    def create_payment(self):
        # Create payment at financial
        bank_payment_id = str(uuid.uuid4())

        #create code
        hash_payment = f'hash_payment_{bank_payment_id}'

        # qr code
        img = qrcode.make(hash_payment)

        # save image as png file
        file_name = f"qr_code_payment_{bank_payment_id}"
        img.save(f"static/img/{file_name}.png")

        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path": file_name
        }
