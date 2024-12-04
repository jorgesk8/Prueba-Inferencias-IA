import cv2

from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("C:/Users/E-PIM_15/OneDrive - GRUPO PLASMA AUTOMATION S.A. DE C.V/Escritorio/Prueba Inferencias IA/models/yolo11n-obb.pt")

# Open the video file
img_path = "C:/Users/E-PIM_15/OneDrive - GRUPO PLASMA AUTOMATION S.A. DE C.V/Escritorio/Prueba Inferencias IA/images/Poligono.jpg"
image = cv2.imread(img_path)
image_resized = cv2.resize(image, (1080, 720))

if image_resized is None:
    print("Error: No se pudo leer imagen")
    exit()

# Run YOLOv8 tracking on the frame, persisting tracks between frames
results = model.predict(image_resized)

# Visualize the results on the frame
annotated_frame = results[0].plot()

# Display the annotated frame
cv2.imshow("YOLO Detection", annotated_frame)

cv2.waitKey(0) #Espera hasta que se pulse cualquier tecla
cv2.destroyAllWindows()