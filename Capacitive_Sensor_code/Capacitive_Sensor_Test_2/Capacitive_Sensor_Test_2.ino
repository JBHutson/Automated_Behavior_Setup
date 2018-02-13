#include <CapacitiveSensor.h>
// initiate globals variables for number of licks, number of loop cycles, two value holders and 
// the capacitive sensor object itself 
int lick1, lick2, lick3;
float curTime1 = 0;
float curTime2 = 0;
float curTime3 = 0;
int hour1, hour2, hour3;
int minute1, minute2, minute3; 
int second1, second2, second3;
int loopCount = 1;
long cs1_1v, cs1_2v, cs2_1v, cs2_2v, cs3_1v, cs3_2v;
String dateTime1, dateTime2, dateTime3;
CapacitiveSensor cs1 = CapacitiveSensor(4, 5);
CapacitiveSensor cs2 = CapacitiveSensor(2, 3);
CapacitiveSensor cs3 = CapacitiveSensor(6, 7);

void setup() {
  // open serial port
  Serial.begin(9600);
}

void loop() {
  // check to see if the loop count is even or odd, if odd, the current value is saved as cs1v
  // if even, the current value is set to cs2v
  if (loopCount % 2 != 0){
    cs1_1v = cs1.capacitiveSensor(80);
    // check to see if the current value is over threshold and previous value was under threshold
    // if so, the licks value is incremented by 1
    if (cs1_1v > 1000 && cs1_2v < 1500){
      curTime1 = millis();
      lick1++;
    }
  } else {
    // check to see if the current value is over threshold and previous value was under threshold
    // if so, the licks value is incremented by 1
    cs1_2v = cs1.capacitiveSensor(80);
    if (cs1_2v > 1000 && cs1_1v < 1500){
      curTime1 = millis();
      lick1++;
    }
  }
   if (loopCount % 2 != 0){
    cs2_1v = cs2.capacitiveSensor(80);
    // check to see if the current value is over threshold and previous value was under threshold
    // if so, the licks value is incremented by 1
    if (cs2_1v > 1000 && cs2_2v < 1500){
      curTime2 = millis();
      lick2++;
    }
  } else {
    // check to see if the current value is over threshold and previous value was under threshold
    // if so, the licks value is incremented by 1
    cs2_2v = cs2.capacitiveSensor(80);
    if (cs2_2v > 1000 && cs2_1v < 1500){
      curTime2 = millis();
      lick2++;
    }
  }
   if (loopCount % 2 != 0){
    cs3_1v = cs3.capacitiveSensor(80);
    // check to see if the current value is over threshold and previous value was under threshold
    // if so, the licks value is incremented by 1
    if (cs3_1v > 1000 && cs3_2v < 1500){
      curTime3 = millis();
      lick3++;
    }
  } else {
    // check to see if the current value is over threshold and previous value was under threshold
    // if so, the licks value is incremented by 1
    cs3_2v = cs3.capacitiveSensor(80);
    if (cs3_2v > 1000 && cs3_1v < 1500){
      curTime3 = millis();
      lick3++;
    }
  }

  // take the milliseconds that the program has been running and transform into hour:min:sec
  second1 = curTime1/1000;
  second1 = round(second1);
  minute1 = floor(second1/60);
  second1 = second1%60;
  hour1 = floor(minute1/60);
  minute1 = minute1%60;
  dateTime1 = String(hour1) + ":" + String(minute1) + ":" + String(second1);
  second2 = curTime2/1000;
  second2 = round(second2);
  minute2 = floor(second2/60);
  second2 = second2%60;
  hour2 = floor(minute2/60);
  minute2 = minute2%60;
  dateTime2 = String(hour2) + ":" + String(minute2) + ":" + String(second2);
  second3 = curTime3/1000;
  second3 = round(second3);
  minute3 = floor(second3/60);
  second3 = second3%60;
  hour3 = floor(minute3/60);
  minute3 = minute3%60;
  dateTime3 = String(hour3) + ":" + String(minute3) + ":" + String(second3);

  
  Serial.print(lick1);
  Serial.print(" , ");
  Serial.print(dateTime1);
  Serial.print(" ; ");
  Serial.print(lick2);
  Serial.print(" , ");
  Serial.print(dateTime2);
  Serial.print(" ; ");
  Serial.print(lick3);
  Serial.print(" , ");
  Serial.println(dateTime3);
  delay(20);
  loopCount++;
}
