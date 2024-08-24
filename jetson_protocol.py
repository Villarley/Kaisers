import cv2
import numpy as np
import requests

esp_url = "http://IP_DEL_ESP:PUERTO/fire_detected"

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_bound = np.array([18, 50, 50])
    upper_bound = np.array([35, 255, 255])

    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    mask = cv2.dilate(mask, None, iterations=2)
    mask = cv2.erode(mask, None, iterations=2)

    # Encontrar contornos
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:  
            # Enviar solicitud HTTP al ESP
            response = requests.get(esp_url)
            print("¡Fuego detectado! Enviando señal al ESP.")
            break

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
