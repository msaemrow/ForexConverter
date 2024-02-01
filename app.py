from flask import Flask, render_template, request, jsonify, redirect
from flask_debugtoolbar import DebugToolbarExtension
from converter import Converter
import secrets

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(16)

app.debug = True
toolbar = DebugToolbarExtension(app)

new_forex_converter = Converter()


@app.route('/')
def forex_converter():
    """renders the initial template with a list of supported currencies"""
    supported_currencies = new_forex_converter.supported_currencies()
    return render_template('converter.html', supported_currencies=supported_currencies)
    

@app.route('/converted', methods=["POST"])
def converted_amount():
    """gathers form data and updates the page with the converted amount"""
    c_from = request.form['convert-from']
    c_to = request.form['convert-to']
    c_amount = request.form['amount']
    converted_amount = round(new_forex_converter.convert_currency(c_from, c_to, float(c_amount)), 2)
    supported_currencies = new_forex_converter.supported_currencies()
    return render_template('converter.html', curr_from=c_from, curr_to=c_to, curr_amount=c_amount, conv_amount=converted_amount, supported_currencies=supported_currencies)
