#define USE_ARDUINO_INTERRUPTS true
#include <PulseSensorPlayground.h>

const int PULSE_INPUT = A0;
const int PULSE_BLINK = 13;
const int THRESHOLD = 550;

PulseSensorPlayground pulseSensor;

void setup() {
 
  Serial.begin(115200);

  pulseSensor.analogInput(PULSE_INPUT);
  pulseSensor.blinkOnPulse(PULSE_BLINK);
  pulseSensor.setThreshold(THRESHOLD);

  pulseSensor.begin();

    
  
}

void loop() {
  delay(20);

  if (pulseSensor.sawStartOfBeat()) {
   Serial.println(pulseSensor.getInterBeatIntervalMs());
  }


}
