#include <Arduino_LSM9DS1.h>

float x, y, z;
float gx, gy, gz;
unsigned long previousMillis = 0;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(112500); // baud rate is 111250 
  while (!Serial);

  if (!IMU.begin()) {
    Serial.print("Failed to initialize IMU! Error");
    while(1);
  }


}

void loop() {
  // put your main code here, to run repeatedly:


  unsigned long currentMillis = millis();

  IMU.readAcceleration(x, y, z);
  IMU.readGyroscope(gx, gy, gz);

  //Serial.print("X Value: ");
  Serial.print(x);
  Serial.print(",");

  //Serial.print("Y Value: ");
  Serial.print(y);
  Serial.print(",");

  //Serial.print("Z Value: ");
  Serial.print(z);
  Serial.println(",");

  Serial.print(gx);
  Serial.println(",");

  Serial.print(gy);
  Serial.println(",");

  Serial.print(gz);
  Serial.println(",");

  //Serial.println("----------");

  delay(500);


}
