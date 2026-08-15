#Crea un sistema de recomendación de películas complejo usando diccionarios
def crear_sistema_recomendacion():
    # Diccionario de películas con sus géneros y calificaciones
    peliculas = {
        "Inception": {"genero": "Ciencia Ficción", "calificacion": 8.8},
        "The Dark Knight": {"genero": "Acción", "calificacion": 9.0},
        "Interstellar": {"genero": "Ciencia Ficción", "calificacion": 8.6},
        "Pulp Fiction": {"genero": "Crimen", "calificacion": 8.9},
        "The Matrix": {"genero": "Ciencia Ficción", "calificacion": 8.7},
        "Forrest Gump": {"genero": "Drama", "calificacion": 8.8},
        "The Shawshank Redemption": {"genero": "Drama", "calificacion": 9.3},
        "The Godfather": {"genero": "Crimen", "calificacion": 9.2},
        "Fight Club": {"genero": "Drama", "calificacion": 8.8},
        "The Lord of the Rings: The Return of the King": {"genero": "Fantasía", "calificacion": 8.9}
    }

    return peliculas

# Crea una función que reciba el diccionario de películas y un género, y devuelva las películas que coincidan con ese género
def recomendar_por_genero(peliculas, genero):
    recomendaciones = {}
    for pelicula, detalles in peliculas.items():
        if detalles["genero"].lower() == genero.lower():
            recomendaciones[pelicula] = detalles
    return recomendaciones

# Crea una función que reciba el diccionario de películas y un rango de calificaciones, y devuelva las películas que estén dentro de ese rango
def recomendar_por_calificacion(peliculas, calificacion_min, calificacion_max):
    recomendaciones = {}
    for pelicula, detalles in peliculas.items():
        if calificacion_min <= detalles["calificacion"] <= calificacion_max:
            recomendaciones[pelicula] = detalles
    return recomendaciones

# Crea una función que reciba el diccionario de películas y un género, y devuelva las películas que coincidan con ese género ordenadas por calificación
def recomendar_por_genero_ordenado(peliculas, genero):
    recomendaciones = {}
    for pelicula, detalles in peliculas.items():
        if detalles["genero"].lower() == genero.lower():
            recomendaciones[pelicula] = detalles
    # Ordenar las recomendaciones por calificación de mayor a menor
    recomendaciones_ordenadas = dict(sorted(recomendaciones.items(), key=lambda item: item[1]["calificacion"], reverse=True))
    return recomendaciones_ordenadas

# Crea una función que reciba el diccionario de películas y un género, y devuelva las películas que coincidan con ese género ordenadas por calificación y filtradas por un rango de calificaciones
def recomendar_por_genero_y_calificacion(peliculas, genero, calificacion_min, calificacion_max):
    recomendaciones = {}
    for pelicula, detalles in peliculas.items():
        if detalles["genero"].lower() == genero.lower() and calificacion_min <= detalles["calificacion"] <= calificacion_max:
            recomendaciones[pelicula] = detalles
    # Ordenar las recomendaciones por calificación de mayor a menor
    recomendaciones_ordenadas = dict(sorted(recomendaciones.items(), key=lambda item: item[1]["calificacion"], reverse=True))
    return recomendaciones_ordenadas

# Ejemplo de uso del sistema de recomendación
if __name__ == "__main__":
    peliculas = crear_sistema_recomendacion()
    
    # Recomendaciones por género
    genero = "Ciencia Ficción"
    print(f"Recomendaciones por género '{genero}':")
    recomendaciones_genero = recomendar_por_genero(peliculas, genero)
    for pelicula, detalles in recomendaciones_genero.items():
        print(f"{pelicula}: {detalles}")
    
    # Recomendaciones por calificación
    calificacion_min = 8.7
    calificacion_max = 9.0
    print(f"\nRecomendaciones por calificación entre {calificacion_min} y {calificacion_max}:")
    recomendaciones_calificacion = recomendar_por_calificacion(peliculas, calificacion_min, calificacion_max)
    for pelicula, detalles in recomendaciones_calificacion.items():
        print(f"{pelicula}: {detalles}")
    
    # Recomendaciones por género ordenadas por calificación
    print(f"\nRecomendaciones por género '{genero}' ordenadas por calificación:")
    recomendaciones_genero_ordenado = recomendar_por_genero_ordenado(peliculas, genero)
    for pelicula, detalles in recomendaciones_genero_ordenado.items():
        print(f"{pelicula}: {detalles}")
    
    # Recomendaciones por género y calificación
    print(f"\nRecomendaciones por género '{genero}' y calificación entre {calificacion_min} y {calificacion_max}:")
    recomendaciones_genero_y_calificacion = recomendar_por_genero_y_calificacion(peliculas, genero, calificacion_min, calificacion_max)
    for pelicula, detalles in recomendaciones_genero_y_calificacion.items():
        print(f"{pelicula}: {detalles}")

    # Recomendaciones por género y calificación con un género que no existe
    genero_inexistente = "Comedia"
    print(f"\nRecomendaciones por género '{genero_inexistente}' y calificación entre {calificacion_min} y {calificacion_max}:")
    recomendaciones_genero_y_calificacion = recomendar_por_genero_y_calificacion(peliculas, genero_inexistente, calificacion_min, calificacion_max)
    for pelicula, detalles in recomendaciones_genero_y_calificacion.items():
        print(f"{pelicula}: {detalles}")


    # Recomendaciones por género y calificación con un rango de calificación que no existe
    calificacion_min_inexistente = 9.5
    calificacion_max_inexistente = 10.0
    print(f"\nRecomendaciones por género '{genero}' y calificación entre {calificacion_min_inexistente} y {calificacion_max_inexistente}:")
    recomendaciones_genero_y_calificacion = recomendar_por_genero_y_calificacion(peliculas, genero, calificacion_min_inexistente, calificacion_max_inexistente)
    for pelicula, detalles in recomendaciones_genero_y_calificacion.items():
        print(f"{pelicula}: {detalles}") 

    # Recomendaciones por género y calificación con un género que no existe y un rango de calificación que no existe
    print(f"\nRecomendaciones por género '{genero_inexistente}' y calificación entre {calificacion_min_inexistente} y {calificacion_max_inexistente}:")
    recomendaciones_genero_y_calificacion = recomendar_por_genero_y_calificacion(peliculas, genero_inexistente, calificacion_min_inexistente, calificacion_max_inexistente)
    for pelicula, detalles in recomendaciones_genero_y_calificacion.items():
        print(f"{pelicula}: {detalles}")
