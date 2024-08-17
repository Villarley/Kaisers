import cv2
import numpy as np

# Cargar el modelo preentrenado MobileNet-SSD
model_path = "ssd_mobilenet_v2_coco_2018_03_29/frozen_inference_graph.pb"
config_path = "ssd_mobilenet_v2_coco_2018_03_29.pbtxt"
net = cv2.dnn_DetectionModel(model_path, config_path)

# Configurar el modelo para trabajar con la GPU de la Jetson Nano
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

# Definir los parámetros de la red
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# Etiquetas de clases del modelo COCO
CLASSES = {0: 'background', 1: 'person', 2: 'bicycle', 3: 'car', ...}

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Realizar la detección de objetos
    class_ids, confidences, boxes = net.detect(frame, confThreshold=0.5)

    # Recorrer las detecciones y etiquetar personas y objetos
    for class_id, confidence, box in zip(class_ids.flatten(), confidences.flatten(), boxes):
        label = CLASSES.get(class_id, "Unknown")
        cv2.rectangle(frame, box, color=(0, 255, 0), thickness=2)
        cv2.putText(frame, f'{label}: {confidence:.2f}', (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

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
