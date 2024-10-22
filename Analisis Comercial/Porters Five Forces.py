import matplotlib.pyplot as plt

# Definir las fuerzas y sus valores (calificación de 1 a 5)
forces = [
    'Amenaza de nuevos entrantes', 
    'Poder de negociación de los proveedores', 
    'Poder de negociación de los clientes', 
    'Amenaza de productos sustitutos', 
    'Rivalidad entre competidores existentes'
]

# Calificaciones hipotéticas basadas en el documento
values = [3, 2, 4, 3, 5]

# Crear el gráfico de barras horizontales
plt.figure(figsize=(10, 6))
plt.barh(forces, values, color='skyblue')
plt.xlabel('Intensidad')
plt.title('Análisis de las Cinco Fuerzas de Porter')
plt.show()

