#include <Servo.h>

Servo servo1;
Servo servo2;

void setup() {
 Serial.begin(38400);
 Serial.setTimeout(10);
}
void loop() {
 while (!Serial.available());
 String req = Serial.readStringUntil('\n');
 if(req.length() > 0 ){
   String servoID = req.substring(0,req.indexOf(":"));
   String value = req.substring(req.indexOf(":") + 1);

   
   if (servoID == "s1") {
    int pos = value.toInt();
    if(pos>0 && pos < 180) {
      servo1.attach(9);
      int currentPos = servo1.read();
      if(pos != currentPos) {
        servo1.write(pos);
        delay(500);
      }
      servo1.detach();
    }
   }
   
   if (servoID == "s2") {
    if (value == "r") {
      
        servo2.attach(10);
        servo2.write(80);
        delay(100);
        servo2.detach();
    
    }
    if (value == "l") {
      
        servo2.attach(10);
        servo2.write(100);
        delay(100);
        servo2.detach();
    
    }
   }
 }
}
