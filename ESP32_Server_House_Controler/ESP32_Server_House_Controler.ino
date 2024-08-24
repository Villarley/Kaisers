#include <WiFi.h>
#include <WebServer.h> 

const char* ssid = "NOMBRE_DE_TU_RED";
const char* password = "CONTRASEÑA_DE_TU_RED";

ESP8266WebServer server(80); // Cambiar a WebServer server(80) para ESP32

void setup() {
  Serial.begin(115200);

  // Conectar a la red WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando a WiFi...");
  }
  Serial.println("Conectado a la WiFi");

  // Configurar la ruta para detectar fuego
  server.on("/fire_detected", []() {
    Serial.println("¡Fuego detectado! Recibido desde Jetson Nano.");
    // Aquí puedes agregar código para encender una alarma o realizar alguna acción
    server.send(200, "text/plain", "Fuego detectado");
  });

  server.begin();
  Serial.println("Servidor iniciado");
}

void loop() {
  server.handleClient();
}
