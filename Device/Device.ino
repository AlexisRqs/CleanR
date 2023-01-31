#define DBG_LED 2

void setup() {
  Serial.begin(9600);
  pinMode(DBG_LED, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    while (Serial.available() > 0) {
      Serial.read();
    }
    char value = (char) (analogRead(A0) / 4);
    Serial.write(value);
    Serial.flush();

    digitalWrite(DBG_LED, HIGH);
    delay(250);
    digitalWrite(DBG_LED, LOW);
  }
  delay(250);
}
