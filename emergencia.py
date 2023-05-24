import numpy as np

def sistema_recomendacion(datos, generos, usuario, k=5):
    # Cálculo de similitud de usuarios basado en el producto de matrices
    similitud = np.dot(datos, datos.T)

    # Cálculo de la similitud del usuario objetivo con otros usuarios
    sim_usuario = similitud[usuario]

    # Obtener los índices de los usuarios más similares
    indices_similares = np.argsort(sim_usuario)[-k-1:-1][::-1]

    # Calcular la puntuación ponderada de cada género para el usuario objetivo
    puntuacion_generos = np.dot(similitud[usuario], datos) / np.sum(similitud[usuario])

    # Eliminar las puntuaciones de los géneros ya vistos por el usuario
    puntuacion_generos[datos[usuario] > 0] = -1

    # Obtener los índices de los géneros más recomendados
    indices_recomendados = np.argsort(puntuacion_generos)[-k:][::-1]

    # Obtener los nombres de los géneros recomendados
    recomendaciones = [generos[i] for i in indices_recomendados]

    return recomendaciones

# Ejemplo de uso
datos = np.array([[4, 5, 0, 1, 0],
                  [5, 4, 3, 2, 1],
                  [0, 2, 4, 0, 5],
                  [1, 0, 5, 4, 2]])

generos = ['Acción', 'Comedia', 'Drama', 'Ciencia ficción', 'Romance']

usuario = 0
recomendaciones = sistema_recomendacion(datos, generos, usuario, k=2)

print("Recomendaciones para el usuario", usuario)
for genero in recomendaciones:
    print("Género:", genero)
