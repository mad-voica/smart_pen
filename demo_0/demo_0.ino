#include <Arduino_LSM9DS1.h>

float x, y, z;
float gx, gy, gz;
float magx, magy, magz;
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
  IMU.readMagneticField(magx, magy, magz);

  //Serial.print("X Value: ");
  Serial.print(x);
  Serial.print(",");

  //Serial.print("Y Value: ");
  Serial.print(y);
  Serial.print(",");

  //Serial.print("Z Value: ");
  Serial.print(z);
  Serial.print(",");

  //Serial.print("Gyro X Value: ");
  Serial.print(gx);
  Serial.print(",");

  //Serial.print("Gyro Y Value: ");
  Serial.print(gy);
  Serial.print(",");

  //Serial.print("Gyro Z Value: ");
  Serial.print(gz);
  Serial.print(",");

  Serial.print(magx);
  Serial.print(",");
  Serial.print(magy);
  Serial.print(",");
  Serial.println(magz);
  //Serial.println(",");\

  //Serial.println("----------");

  delay(100);


}
