from flask import Flask, jsonify, request

app = Flask(__name__)

# exchange rate
def USDtoEuroRate():
    return 0.94  

@app.route('/<usd>', methods=['GET'])
def convert_usd_to_euro(usd):
    # usd = request.args.get('amount', default=1, type=float)
    exchangeRate = USDtoEuroRate()
    euros = float(usd) * exchangeRate
    return jsonify({
        'usd': usd,
        'euros': round(euros, 2),
        'exchangeRate': exchangeRate
    })

if __name__ == '__main__':
    app.run(debug=True, port=8006)