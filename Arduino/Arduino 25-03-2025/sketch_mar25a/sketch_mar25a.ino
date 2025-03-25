#define trig 7
#define echo 8
int dist = 0;
int ledG = 10;
int ledY = 11;
int ledR = 12;

void setup() {
  pinMode(trig, OUTPUT);
  pinMode(ledG, OUTPUT);
  pinMode(ledY, OUTPUT);
  pinMode(ledR, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  dist = pulseIn(echo, HIGH);
  dist = dist / 58;
  Serial.println("distância: "+ String(dist));

  if(dist<=15){
    digitalWrite(ledR, HIGH);
    digitalWrite(ledY, LOW);
    digitalWrite(ledG, LOW);
  }
  else if(dist>15&&dist<=30){
    digitalWrite(ledR, LOW);
    digitalWrite(ledY, HIGH);
    digitalWrite(ledG, LOW);
    }
  else if(dist>30){
    digitalWrite(ledR, LOW);
    digitalWrite(ledY, LOW);
    digitalWrite(ledG, HIGH);
  }
}