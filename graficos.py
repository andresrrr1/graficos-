import numpy as np
import matplotlib.pyplot as plt

# Parámetros para la espiral
t = np.linspace(0, 10*np.pi, 1000)  #1000 puntos a lo largo de la espiral
x = t * np.cos(t)
y = t * np.sin(t)
z = t

# Creacion la figura 
figura = plt.figure() #es una figura vacía en la que se pueden trazar gráficos.
a = figura.add_subplot(111, projection='3d')  #es una cuadrícula de figuras que se crean dentro de una sola figura
# Graficar la espiral
plt.plot(x, y, z)

# Configuraciones del gráfico
plt.xlabel('x')
plt.ylabel('y')
plt.zlabel('z')
plt.title('espiral')
plt.grid(True) # Habilita la cuadrícula en el gráfico
plt.axis('equal')  # Asegura que los ejes tengan la misma escala y longitud en todas las direcciones.
plt.show()


