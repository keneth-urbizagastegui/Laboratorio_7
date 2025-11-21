from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Consumir la API de tasas de cambio
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
        
        # Extraer los valores de EUR y PEN
        eur_rate = data['rates']['EUR']
        pen_rate = data['rates']['PEN']
        
        # Preparar los datos para el template
        exchange_rates = {
            'USD': 1.0,
            'EUR': eur_rate,
            'PEN': pen_rate
        }
        
        return render_template('index.html', rates=exchange_rates)
    
    except Exception as e:
        # En caso de error, mostrar valores por defecto
        exchange_rates = {
            'USD': 1.0,
            'EUR': 0.85,  # Valor aproximado por defecto
            'PEN': 3.80   # Valor aproximado por defecto
        }
        return render_template('index.html', rates=exchange_rates, error=True)

if __name__ == '__main__':
    app.run(debug=True)