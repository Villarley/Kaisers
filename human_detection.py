import cv4

# Inicializar el detector HOG con el clasificador preentrenado para humanos
hog = cv4.HOGDescriptor()
hog.setSVMDetector(cv4.HOGDescriptor_getDefaultPeopleDetector())

# Capturar video desde la cámara
cap = cv4.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Redimensionar la imagen para mejorar la velocidad de procesamiento
    frame = cv4.resize(frame, (640, 480))

    # Detectar personas en el fotograma
    (rects, _) = hog.detectMultiScale(frame, winStride=(4, 4),
                                      padding=(8, 8), scale=1.05)

    # Dibujar los cuadros alrededor de las detecciones
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar el resultado
    cv4.imshow('Detección de Humanos', frame)

    # Presiona 'q' para salir
    if cv4.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv4.destroyAllWindows()