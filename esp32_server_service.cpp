#include <WiFi.h>

const char* ssid = "";       // Reemplaza con el SSID de tu red Wi-Fi
const char* password = ""; // Reemplaza con la contraseña de tu red Wi-Fi

WiFiServer server(80); // El servidor escucha en el puerto 80

void setup() {
  Serial.begin(9600);

  // Conectar a la red Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando a WiFi...");
  }
  Serial.println("Conectado a la red Wi-Fi");

  // Imprimir la dirección IP
  Serial.print("Dirección IP del ESP32: ");
  Serial.println(WiFi.localIP());

  // Iniciar el servidor
  server.begin();
  Serial.println("Servidor TCP iniciado");
}

void loop() {
  WiFiClient client = server.available();   // Esperar por un cliente
  if (client) {                             // Si se conecta un cliente
    Serial.println("Cliente conectado");
    while (client.connected()) {
      if (client.available()) {             // Si hay datos para leer
        String data = client.readStringUntil('\n'); // Leer los datos
        Serial.println("Recibido: " + data);

        // Responder al cliente
        client.println("Instrucción recibida: " + data);
      }
    }
    client.stop();
    Serial.println("Cliente desconectado");
  }
}