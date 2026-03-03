//Using DHT for temperature and humidity tests

#include <DHT.h>

#define dhtPin 2
#define dhtType DHT11

DHT dht(dhtPin, dhtType);
int ledG = 10;
int ledY = 11;
int ledR = 12;

void setup(){
Serial.begin(9600);
dht.begin();
pinMode(ledG, OUTPUT);
pinMode(ledY, OUTPUT);
pinMode(ledR, OUTPUT);
}
void loop(){
int temp = dht.readTemperature();
int umi = dht.readHumidity();
Serial.println("Temperatura: " + String(temp));
Serial.println("Umidade: " + String(umi));

  if(temp<=15&&umi<=20){
    digitalWrite(ledR, HIGH);
    digitalWrite(ledY, LOW);
    digitalWrite(ledG, LOW);
  }
  else if(temp>15&&temp<30&&umi>20&&umi<40){
    digitalWrite(ledR, LOW);
    digitalWrite(ledY, HIGH);
    digitalWrite(ledG, LOW);
    }
  else if(temp>30&&umi>60){
    digitalWrite(ledR, LOW);
    digitalWrite(ledY, LOW);
    digitalWrite(ledG, HIGH);
    
  }
}
