import cv2  
import numpy as np 
import os

def fnGetWebcam(imagenPNG="tubo"):

    version = 1
    while os.path.exists(f"{imagenPNG}{version}.png"):
        version +=1

    # Inicializar la càmera
    cap = cv2.VideoCapture(0)  # 0 indica la primera cámara disponible, puede variar
    # Establecer la resolución deseada
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 848)  # Ancho
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Alto

    # Capturar una imagen
    ret, frame = cap.read()
    if not ret:
        print("Error al capturar imagen")
        cap.release()
        return



    # # Aumentamos brillo
    # increment_brillantor = 0
    # frame_brillant = cv2.addWeighted(frame, 1 + increment_brillantor / 100, np.zeros_like(frame), 0, 0)

 
    cv2.imwrite(imagenPNG +f'{version}.png', frame, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
   

    # Liberar recursos
    cap.release()

while True:
    capturar = str(input("Presione 's' para capturar: "))

    if capturar == 's':
        fnGetWebcam()
    elif capturar == 'q':
        break

