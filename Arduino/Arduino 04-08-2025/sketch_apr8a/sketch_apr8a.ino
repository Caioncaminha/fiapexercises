#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);


void setup() {
  Serial.begin(9600);
lcd.init();
lcd.backlight();
lcd.begin(16,2);
lcd.setCursor(1,0);
lcd.print("Eitapola");
lcd.print(".");
delay(1000);
lcd.print(".");
delay(1000);
lcd.print(".");
delay(1000);
lcd.clear();


}

void loop() {


}
