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
    # Grafico 1
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
    plt.title('Trabajos destruidos vs Trabajos creados')
    plt.xticks(x, df['Year'])
    plt.legend()
    
    plt.savefig('static/images/plot.png')
    plt.close()
    
    #Grafico 2
    df['AI Adoption (%)'] = df['AI Adoption (%)'].str.replace('%', '').astype(float)
    
    x = df['Year']
    y = df['AI Adoption (%)']
    
    plt.plot(x,y, color='green', label='Evolution of AI use', linewidth=1.5)
    plt.xlabel('Year')
    plt.ylabel('AI Adoption (%)')
    plt.title('Uso de IA en el Entorno Empresarial a Través del Tiempo')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('static/images/plot2.png')
    plt.close()
    
    #Grafico 3
    
    df['Organizations Using AI'] = df['Organizations Using AI'].str.replace('%', '').astype(float)
    df['Organizations Planning to Implement AI'] = df['Organizations Planning to Implement AI'].str.replace('%', '').astype(float)
    
    x = df['Year']
    y = df['Organizations Using AI']
    z = df['Organizations Planning to Implement AI']
    
    plt.plot(x,y, color='green', label='Using AI', linewidth=1.5)
    plt.plot(x,z, color='red', label='Planning to Implement AI',linewidth=1.5)
    plt.xlabel('Year')
    plt.ylabel('Use of AI (%)')
    plt.title('Empresas que Usan y que Planean Usar')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('static/images/plot3.png')
    plt.close()

    # Grafico 4
    years = list(range(1956, 2024))

    progress = []

    for year in years:
        if 1956 <= year < 1970:
            progress.append(10)  # Avances iniciales lentos
        elif 1970 <= year < 1980:
            progress.append(20)  # Primer invierno de la IA
        elif 1980 <= year < 1987:
            progress.append(30)  # Salida del primer invierno, pequeños avances
        elif 1987 <= year < 1993:
            progress.append(30)  # Segundo invierno de la IA
        elif 1993 <= year < 1997:
            progress.append(35)  # Final del segundo invierno, avances moderados
        elif 1997 <= year < 2006:
            progress.append(45)  # Avances tras Deep Blue
        elif 2006 <= year < 2012:
            progress.append(60)  # Avances en redes neuronales profundas
        elif 2012 <= year < 2018:
            progress.append(75)  # Grandes avances en reconocimiento de imagen y NLP
        elif 2018 <= year < 2021:
            progress.append(85)  # Modelos generativos (GPT-3)
        elif 2021 <= year <= 2023:
            progress.append(95)  # GPT-4 y DALL-E 3
        else:
            progress.append(100)  # Estado actual de la IA en 2023

    plt.figure(figsize=(10, 6))
    plt.plot(years, progress, marker='o', linestyle='-', color='b')

    plt.title('Progreso de la Inteligencia Artificial (1956-2023)')
    plt.xlabel('Años')
    plt.ylabel('Progreso de la IA (escala de 0 a 100)')
    plt.grid(True)

    plt.savefig('static/images/plot4.png')
    plt.close()
    return render_template('analysis.html')
    
if __name__ =='__main__':
    # El modo debug reinicia automáticamente el servidor al hacer cambios,
    # pero es necesario recargar la página en el navegador para ver esos cambios.
    app.run(debug=True)
 
