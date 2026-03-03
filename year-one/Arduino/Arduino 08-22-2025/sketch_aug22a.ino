#include <ArduinoJson.h>
#include <DHT.h>

StaticJsonDocument<16> info;
DHT dht(7, DHT11);

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(13, OUTPUT);

}

void loop() {
  String output;
  info["temperatura"] = dht.readTemperature();
  info["umidade"] = dht.readHumidity();

  serializeJson(info, output);
  Serial.println(output);
  delay(1000);
  digitalWrite(13, HIGH);
  delay(500);
  digitalWrite(13, LOW);
}
