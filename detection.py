import cv2
import numpy as np

# Cargar el modelo preentrenado MobileNet-SSD
net = cv2.dnn.readNetFromTensorflow('ssd_mobilenet_v2_coco.pb', 'ssd_mobilenet_v2_coco.pbtxt')

# Si tienes CUDA instalada, habilitarla
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

# Etiquetas de clases del modelo COCO
CLASSES = {0: 'background', 1: 'person', 2: 'bicycle', 3: 'car'}

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preparar el frame para la detección
    blob = cv2.dnn.blobFromImage(frame, 1.0/127.5, (320, 320), (127.5, 127.5, 127.5), swapRB=True, crop=False)
    net.setInput(blob)
    
    # Realizar la detección
    detections = net.forward()

    # Recorrer las detecciones
    for detection in detections[0, 0, :, :]:
        confidence = float(detection[2])
        if confidence > 0.5:
            class_id = int(detection[1])
            box = detection[3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
            (startX, startY, endX, endY) = box.astype("int")
            label = CLASSES.get(class_id, "Unknown")
            
            cv2.rectangle(frame, (startX, startY), (endX, endY), color=(0, 255, 0), thickness=2)
            cv2.putText(frame, f'{label}: {confidence:.2f}', (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            if label == 'person':
                print("¡Persona detectada!")
            else:
                print("¡Objeto detectado!")

    # Mostrar la imagen con las detecciones
    cv2.imshow("Detección de Personas y Objetos", frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
