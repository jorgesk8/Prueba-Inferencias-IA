import cv2

def obtener_resolucion(ruta_imagen):
    # Cargar la imagen
    imagen = cv2.imread(ruta_imagen)
    
    if imagen is None:
        print("Error: No se pudo cargar la imagen. Verifica la ruta.")
        return None
    
    # Obtener las dimensiones de la imagen
    altura, ancho, _ = imagen.shape
    
    # Devolver la resolución
    return ancho, altura

# Ruta de la imagen
ruta_imagen = "C:/Users/E-PIM_15/OneDrive - GRUPO PLASMA AUTOMATION S.A. DE C.V/Escritorio/Prueba Inferencias IA/images/Poligono.jpg"

# Obtener la resolución
resolucion = obtener_resolucion(ruta_imagen)

if resolucion:
    print(f"La resolución de la imagen es: {resolucion[0]}x{resolucion[1]} píxeles")
