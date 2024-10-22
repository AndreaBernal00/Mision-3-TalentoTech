import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
plt.show()
