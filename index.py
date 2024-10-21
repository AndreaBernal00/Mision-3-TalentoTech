import os 
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template

#Creando una app (objeto) a partir de una clase(Flask)
#para poder controlar nuestra aplicación y desplegarla 
#correctamente
app = Flask(__name__)
    
@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

""" @app.route('/analysis')
def analysis():
    return render_template('analysis.html') """
    

if __name__ =='__main__':
    # El modo debug reinicia automáticamente el servidor al hacer cambios,
    # pero es necesario recargar la página en el navegador para ver esos cambios.
    app.run(debug=True)
 
