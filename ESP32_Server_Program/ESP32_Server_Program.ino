#include <WiFi.h>
#include <ESP32Servo.h>

const char* ssid = "CI2A_STEAM";       // Reemplaza con el SSID de tu red Wi-Fi
const char* password = "Cia$_2022"; // Reemplaza con la contraseña de tu red Wi-Fi

Servo myServo;
int buzzerPin = 23;
//int emergency[] = {2,3,4,5,6};
//int normal[] = {9,10,11,12,13};
int ledN1 = 2;
int ledN2 = 4;
int ledN3 = 16;
int ledN4 = 17;
int ledN5 = 5;
int ledE1 = 18;
int ledE2 = 19;
int ledE3 = 21;
int ledE4 = 15;
int ledE5 = 0;
int serv = 15;
WiFiServer server(80); // El servidor escucha en el puerto 80

void setup() {
  Serial.begin(9600);

  myServo.attach(serv);
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledN1, OUTPUT);
  pinMode(ledN2, OUTPUT);
  pinMode(ledN3, OUTPUT);
  pinMode(ledN4, OUTPUT);
  pinMode(ledN5, OUTPUT);
  pinMode(ledE1, OUTPUT);
  pinMode(ledE2, OUTPUT);
  pinMode(ledE3, OUTPUT);
  pinMode(ledE4, OUTPUT);
  pinMode(ledE5, OUTPUT);
  digitalWrite(ledN1,HIGH);
  digitalWrite(ledN2,HIGH);
  digitalWrite(ledN3,HIGH);
  digitalWrite(ledN4,HIGH);
  digitalWrite(ledN5,HIGH);
  digitalWrite(ledE1,LOW);
    digitalWrite(ledE2,LOW);
    digitalWrite(ledE3,LOW);
    digitalWrite(ledE4,LOW);
    digitalWrite(ledE5,LOW);
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
    digitalWrite(ledN1,LOW);
    digitalWrite(ledN2,LOW);
    digitalWrite(ledN3,LOW);
    digitalWrite(ledN4,LOW);
    digitalWrite(ledN5,LOW);
    digitalWrite(ledE1,HIGH);
    digitalWrite(ledE2,HIGH);
    digitalWrite(ledE3,HIGH);
    digitalWrite(ledE4,HIGH);
    digitalWrite(ledE5,HIGH);
    tone(buzzerPin, 800);
    delay(2500);
    noTone(buzzerPin);
    delay(1000); 
    tone(buzzerPin, 800);
    delay(2500);
    noTone(buzzerPin);
    delay(1000); 
    tone(buzzerPin, 800);
    delay(2500);
    noTone(buzzerPin);
    delay(1000); 
  //}
}