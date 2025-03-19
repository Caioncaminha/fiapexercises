int ledY = 9;
int x = 0;

void setup() {
 pinMode(ledY, OUTPUT);
}

void loop() {
 for(x = 0; x < 3; x++){ //Letra S
  digitalWrite(ledY, HIGH);
  delay(100);
  digitalWrite(ledY, LOW);
  delay(500);
 }

 for(x = 0; x < 3; x++){ //Letra O
  digitalWrite(ledY, HIGH);
  delay(1000);
  digitalWrite(ledY, LOW);
  delay(500);
 }
}
