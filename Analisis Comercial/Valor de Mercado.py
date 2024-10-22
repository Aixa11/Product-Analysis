import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Datos de empresas relevadas del documento
data = {
    'Empresa': ['Earth Optics', 'EOS', 'AgroMapas', 'EasyAgro'],
    'Tamaño_Ha': [10000, 10000, 500, 1000],
    'Precio_Producto': [34, 1, 0, 48],  # USD por Ha (algunos datos son ficticios ya que no se especificaron en el documento)
    'Ingresos_Anuales': [340000, 10000, 0, 48000]  # USD (ficticios para el ejemplo)
}

# Crear DataFrame
df = pd.DataFrame(data)

# Modelo de regresión lineal para estimar el valor de mercado inicial
X = df[['Tamaño_Ha', 'Precio_Producto']]
y = df['Ingresos_Anuales']

# Entrenar el modelo
model = LinearRegression()
model.fit(X, y)

# Predecir ingresos anuales para un tamaño y precio dado
nueva_empresa = {'Tamaño_Ha': 8000, 'Precio_Producto': 35}
nueva_empresa_ingresos = model.predict(np.array([[nueva_empresa['Tamaño_Ha'], nueva_empresa['Precio_Producto']]]))[0]

print(f"Valor de Mercado Inicial Estimado para la nueva empresa: USD {nueva_empresa_ingresos:.2f}")

# Visualización
plt.scatter(df['Tamaño_Ha'], df['Ingresos_Anuales'], color='blue')
plt.plot(df['Tamaño_Ha'], model.predict(X), color='red')
plt.xlabel('Tamaño (Ha)')
plt.ylabel('Ingresos Anuales (USD)')
plt.title('Estimación de Ingresos Anuales')
plt.show()

