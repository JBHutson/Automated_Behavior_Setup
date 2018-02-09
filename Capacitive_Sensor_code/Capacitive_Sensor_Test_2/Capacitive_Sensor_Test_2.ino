#include <CapacitiveSensor.h>
// initiate globals variables for number of licks, number of loop cycles, two value holders and 
// the capacitive sensor object itself 
int lick;
float curTime = 0;
int hour;
int minute; 
int second;
int loopCount = 1;
long cs1v, cs2v;
String dateTime;
CapacitiveSensor cs1 = CapacitiveSensor(4, 5);

void setup() {
  // open serial port
  Serial.begin(9600);
}

void loop() {
  // check to see if the loop count is even or odd, if odd, the current value is saved as cs1v
  // if even, the current value is set to cs2v
  if (loopCount % 2 != 0){
    cs1v = cs1.capacitiveSensor(80);
    // check to see if the current value is over threshold and previous value was under threshold
    // if so, the licks value is incremented by 1
    if (cs1v > 1000 && cs2v < 1500){
      curTime = millis();
      lick++;
    }
  } else {
    // check to see if the current value is over threshold and previous value was under threshold
    // if so, the licks value is incremented by 1
    cs2v = cs1.capacitiveSensor(80);
    if (cs2v > 1000 && cs1v < 1500){
      curTime = millis();
      lick++;
    }
  }

  // take the milliseconds that the program has been running and transform into hour:min:sec
  second = curTime/1000;
  second = round(second);
  minute = floor(second/60);
  second = second%60;
  hour = floor(minute/60);
  minute = minute%60;
  dateTime = String(hour) + ":" + String(minute) + ":" + String(second);

  
  Serial.print(lick);
  Serial.print(" , ");
  Serial.println(dateTime);
  delay(20);
  loopCount++;
}
