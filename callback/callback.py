import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback():
    token = 'ВАШ ТОКЕН'

    sign = request.headers.get('Signature')
    sign2 =
hashlib.sha256(f"{request.form['id']}|{request.form['createdDateTime']}|{request.form['amount']}".encode('utf-8') +
token.encode('utf-8')).hexdigest()
    if sign != sign2:
        return 'ERROR SIGN', 400

    id = request.form['id']
    order_id = request.form['order_id']
    amount = request.form['amount']
    in_amount = request.form['in_amount']
    data = request.form['data']
    createdDateTime = request.form['createdDateTime']
    status = request.form['status']


    return 'OK', 200

if __name__ == '__main__':
    app.run()
