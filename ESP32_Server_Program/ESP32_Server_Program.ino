#include <WiFi.h>
#include <ESP32Servo.h>

const char* ssid = "Redmi";       // Reemplaza con el SSID de tu red Wi-Fi
const char* password = "TRIKSY2530"; // Reemplaza con la contraseña de tu red Wi-Fi

Servo myServo; 
//int emergency[] = {2,3,4,5,6};
//int normal[] = {9,10,11,12,13};
int led = 2;
int serv = 15;
WiFiServer server(80); // El servidor escucha en el puerto 80

void setup() {
  Serial.begin(9600);

  myServo.attach(serv);
  pinMode(led, OUTPUT);
  digitalWrite(led,HIGH);
  //for (int i = 0; i < 5; i++) {
    //pinMode(emergency[i], OUTPUT);
    //pinMode(normal[i], OUTPUT);
    
  //}
  //for (int i = 0; i < 5; i++) {
      //digitalWrite(emergency[i], LOW);    
      //digitalWrite(normal[i], HIGH);   
  //}

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
        data.trim(); // Elimina espacios en blanco y caracteres de nueva línea
        // Utiliza if-else en lugar de switch
        if (data == "1") {
          sismic_protocol();
        } else if (data == "2") {
          // Otro protocolo o acción para el caso 2
        } else if (data == "3") {
          // Otro protocolo o acción para el caso 3
        } else {
          // Acción por defecto si no coincide con ningún caso
        }
        // Responder al cliente
        
      }
    }
    client.stop();
    Serial.println("Cliente desconectado");
  }


}

void sismic_protocol(){
  //for (int i = 0; i < 5; i++) {
    //  digitalWrite(emergency[i], HIGH);    
     // digitalWrite(normal[i], LOW);
    myServo.write(90);
    digitalWrite(led,LOW);
    Serial.print("Hola Mundo");
  //}
}