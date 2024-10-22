import os 
import numpy as np
import pandas as pd
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

@app.route('/analysis')
def analysis():
    df = pd.read_csv('csv/ia.csv')
    df['Estimated Jobs Eliminated by AI (millions)'] = df['Estimated Jobs Eliminated by AI (millions)'].str.replace('%', '').astype(float)
    df['Estimated New Jobs Created by AI (millions)'] = df['Estimated New Jobs Created by AI (millions)'].str.replace('%', '').astype(float)
    
    x = np.arange(len(df['Year'])) 
    y = df['Estimated Jobs Eliminated by AI (millions)']
    z = df['Estimated New Jobs Created by AI (millions)']
    
    ancho = 0.35
    
    plt.bar(x - ancho/2, z, width=ancho, color='green', label='New Jobs Created by AI')
    plt.bar(x + ancho/2, y, width=ancho, color='red', label='Jobs Eliminated by AI')
    
    plt.xlabel('Year')
    plt.ylabel('Jobs (millions)')
    plt.title('Impacto de la IA en los trabajos')
    plt.xticks(x, df['Year'])
    plt.legend()
    
    plt.savefig('static/images/plot.png')
    plt.close()
    return render_template('analysis.html')
    

if __name__ =='__main__':
    # El modo debug reinicia automáticamente el servidor al hacer cambios,
    # pero es necesario recargar la página en el navegador para ver esos cambios.
    app.run(debug=True)
 
