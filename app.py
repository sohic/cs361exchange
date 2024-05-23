from flask import Flask, jsonify, request
import re

app = Flask(__name__)

# exchange rate
def USDtoEuroRate():
    return 0.94  

def valid_input(usd):
    valid_format = r'^(\d+)(\.\d{2})?$'
    
    usd_str = str(usd)
    match = re.match(valid_format, usd_str)
    
    if match:
        decimal_part = match.group(2)
        return bool(decimal_part)
    else:
        return False

@app.route('/convert', methods=['GET'])
def convert_usd_to_euro():
    usd = request.args.get('usd', default=None, type=float)
    if usd is None:
        return "Please enter a valid US Dollar value to convert to Euros.", 400, {'Content-Type': 'text/plain'}
    if not valid_input(str(usd)):
        return "Invalid input, please enter a valid dollar amount with exactly two decimal place values.", 400, {'Content-Type': 'text/plain'}
    exchangeRate = USDtoEuroRate()
    euros = float(usd) * exchangeRate
    return jsonify({
        'usd': usd,
        'euros': round(euros, 2),
        'exchangeRate': exchangeRate
    })
    
@app.route('/ping')
def ping():
    return "pong"


if __name__ == '__main__':
    app.run(debug=True, port=8006)