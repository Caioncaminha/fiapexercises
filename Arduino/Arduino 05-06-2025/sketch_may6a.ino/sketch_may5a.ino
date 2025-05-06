// Arduino 05-06-2025
// Projeto: Sensor de Temperatura, Umidade e Luz com LEDs Indicadores
// Descrição: Este código lê os valores de temperatura, umidade e luz de sensores e acende LEDs de acordo com as condições especificadas.

#include <LiquidCrystal_I2C.h>
#include <DHT.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);

#define dhtPin 12
#define dhtType DHT22
DHT dht(dhtPin, dhtType);

#define ldrPin A0
#define led1 11
#define led2 10
#define led3 9

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  dht.begin();

  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(ldrPin, INPUT);
}

void loop() {
  float temp = dht.readTemperature();
  float umi = dht.readHumidity();
  int ldrStatus = analogRead(ldrPin); // 0 (claro) a 1023 (escuro)

  // Apaga os LEDs de começo
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);

  // Regras do DHT e do LDR
  if (
  temp < 11 || temp > 18 ||       // Temperatura fora da faixa ideal
  umi < 60 || umi > 80 ||        // Umidade fora da faixa ideal
  ldrStatus < 300){             // Luz forte
    digitalWrite(led1, HIGH);
  }

  if (
    (temp >= 11 && temp <= 12.9) || (temp >= 13.1 && temp <= 15) ||    // Temperatura intermediária
    (umi > 60 && umi <= 65) || (umi > 75 && umi <= 80) ||             // Umidade intermediária
    (ldrStatus >= 300 && ldrStatus <= 700)){                         // Luz média
    digitalWrite(led2, HIGH);
  }

  if (
    temp == 13 ||                                           // Temperatura ideal
    (umi > 65 && umi <= 70) || (umi > 70 && umi <= 75) ||  // Umidade ideal
    ldrStatus > 700){                                     // Luz baixa
    digitalWrite(led3, HIGH);
  }

  // LCD para display das informações do DHT e LDR.
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(temp);
  lcd.print(" C   ");

  lcd.setCursor(0, 1);
  lcd.print("Umi: ");
  lcd.print(umi);
  lcd.print(" %   ");

  lcd.setCursor(0, 2);
  lcd.print("Luz: ");
  lcd.print(ldrStatus);

  // Serial Monitor test
  Serial.print("Temp: "); Serial.print(temp); Serial.print(" C | ");
  Serial.print("Umi: "); Serial.print(umi); Serial.print(" % | ");
  Serial.print("LDR: "); Serial.println(ldrStatus);

  delay(1000);
}