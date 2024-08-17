import cv2

def main():
    # Intenta abrir la cámara
    cap = cv2.VideoCapture(0)  # Usa el índice 0 para la primera cámara conectada

    if not cap.isOpened():
        print("No se pudo acceder a la cámara.")
        return

    print("Cámara abierta exitosamente. Presiona 'q' para salir.")

    while True:
        # Captura frame por frame
        ret, frame = cap.read()

        if not ret:
            print("No se pudo capturar el frame.")
            break

        # Muestra el frame capturado en una ventana
        cv2.imshow('Video en Vivo', frame)

        # Salir del loop si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera la cámara y cierra las ventanas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
