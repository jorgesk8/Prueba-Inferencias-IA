from collections import defaultdict
import cv2
import numpy as np
from ultralytics import YOLO
from realsense_depth import *

class InferenciaVideo:
    def __init__(self):
        self.w, self.h = (848, 480)# Resolucion
        self.cx = int(self.w / 2)  # Centro en x
        self.cy = int(self.h / 2)  # Centro en y
        self.conf = 0.3  # Confidence threshold
        self.iou = 0.5   # IOU threshold
        
        
    def SeleccionarCam(self):
        # Inicializar la cámara de profundidad RealSense
        camara = DepthCamera()
        return camara
            

    def Modelo(self):
        # Cargar el modelo YOLOv8
        model_path = "C:/Users/E-PIM_15/OneDrive - GRUPO PLASMA AUTOMATION S.A. DE C.V/Escritorio/Prueba Tubos IA/models/tubo_model_conveyo3.pt"
        model = YOLO(model_path)
        return model
    
    def main(self):
        camara = self.SeleccionarCam()
        model = self.Modelo()


        # Loop through the video frames
        while True:
            ret, depth_frame, frame, _ = camara.get_frame()

            if ret:
                track_history = defaultdict(lambda: [])
                
                # Inferencia y seguimiento con YOLOv8 en el frame
                results = model.track(frame, conf=self.conf, iou=self.iou, persist=True, verbose=False)

                # Visualizar los resultados en el frame
                annotated_frame = results[0].plot()

                try:
                    # Obtener las cajas y los IDs de seguimiento
                    boxes = results[0].boxes.xywh.cpu()
                    track_ids = results[0].boxes.id.int().cpu().tolist()

                    # Dibujar las líneas de seguimiento
                    for box, track_id in zip(boxes, track_ids):
                        x, y, w, h = box
                        track = track_history[track_id]
                        track.append((float(x), float(y)))  # Punto central x, y
                        if len(track) > 30:  # Retener 30 tracks para 30 frames
                            track.pop(0)

                        # Dibujar las líneas de tracking
                        points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
                        cv2.polylines(annotated_frame, [points], isClosed=False, color=(230, 230, 230), thickness=2)

                except Exception as e:
                    print("Error: ", e)

                # Mostrar el frame anotado
                cv2.imshow("YOLOv8 Tracking", annotated_frame)

                # Salir del loop si se presiona 'q'
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
                print("No se pudo obtener el frame de la cámara.")
                break

        # Release the video capture object and close the display window
        camara.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    detector = InferenciaVideo()
    try:
        detector.main()
    except Exception as e:
        print("Error: ", e)