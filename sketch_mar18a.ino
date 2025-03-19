int ledY = 8;
int x = 0;

//F . . _ .
//I . .
//A . _
//P . _ _ .

void setup() {
pinMode(ledY, OUTPUT);

}

void loop() {
  delay(1500);
 for(x = 0; x < 2; x++){ //Letra F
  digitalWrite(ledY, HIGH);
  delay(100);
  digitalWrite(ledY, LOW);
  delay(500);
 }
  digitalWrite(ledY, HIGH);
  delay(800);
  digitalWrite(ledY, LOW);
  delay(500);
  digitalWrite(ledY, HIGH);
  delay(100);
  digitalWrite(ledY, LOW);
  delay(1500);
 
 for(x = 2; x < 4; x++){ //Letra I
  digitalWrite(ledY, HIGH);
  delay(100);
  digitalWrite(ledY, LOW);
  delay(500);
 }
  delay(1500);
 for(x = 4; x < 5; x++){ //Letra A
  digitalWrite(ledY, HIGH);
  delay(100);
  digitalWrite(ledY, LOW);
  delay(500);
  digitalWrite(ledY, HIGH);
  delay(800);
  digitalWrite(ledY, LOW);
  delay(1500);
 }

  digitalWrite(ledY, HIGH); //Letra P
  delay(100);
  digitalWrite(ledY, LOW);
  delay(500);
 for(x = 5; x < 7; x++){ 
  digitalWrite(ledY, HIGH);
  delay(800);
  digitalWrite(ledY, LOW);
  delay(500);
 }
  digitalWrite(ledY, HIGH);
  delay(100);
  digitalWrite(ledY, LOW);
  delay(1500);
}
