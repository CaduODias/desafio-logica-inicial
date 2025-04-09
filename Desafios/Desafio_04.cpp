const int pinoTMP = A0;
const int pinoMotor = 8;
const int pinoLed = 11;
const int pinoBuzzer = 9;

void setup() {
  pinMode(pinoMotor, OUTPUT);
  pinMode(pinoLed, OUTPUT);
  pinMode(pinoBuzzer, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int leitura = analogRead(pinoTMP);
  float tensao = leitura * 5.0 / 1024.0;
  float temperatura = (tensao - 0.5) * 100.0; // Conversão para TMP36

  Serial.print("Temperatura: ");
  Serial.println(temperatura);

  // Aciona motor se temperatura >= 30°C
  if (temperatura >= 30.0) {
    digitalWrite(pinoMotor, HIGH);
  } else {
    digitalWrite(pinoMotor, LOW);
  }

  // Alerta de emergência se temperatura > 50°C
  if (temperatura > 50.0) {
    digitalWrite(pinoLed, HIGH);
    digitalWrite(pinoBuzzer, HIGH);
  } else {
    digitalWrite(pinoLed, LOW);
    digitalWrite(pinoBuzzer, LOW);
  }

  delay(1000);
}
