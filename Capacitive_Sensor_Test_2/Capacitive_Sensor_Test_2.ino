// arduino code that creates and runs multiple capacitive circut lick-o-meters simultaniously

#include <CapacitiveSensor.h>
// initiate globals variables for number of licks, number of loop cycles, two value holders and
// the capacitive sensor object itself
int lick1, lick2, lick3;
int loopCount = 1;
long cs1_1v, cs1_2v, cs2_1v, cs2_2v, cs3_1v, cs3_2v;
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
    if (cs1_1v > 40 && cs1_2v < 80){
      lick1++;
    }
  } else {
    // check to see if the current value is over threshold and previous value was under threshold
    // if so, the licks value is incremented by 1
    cs1_2v = cs1.capacitiveSensor(80);
    if (cs1_2v > 40 && cs1_1v < 80){
      lick1++;
    }
  }
   if (loopCount % 2 != 0){
    cs2_1v = cs2.capacitiveSensor(80);
    if (cs2_1v > 40 && cs2_2v < 80){
      lick2++;
    }
  } else {
    cs2_2v = cs2.capacitiveSensor(80);
    if (cs2_2v > 1000 && cs2_1v < 1500){
      lick2++;
    }
  }
   if (loopCount % 2 != 0){
    cs3_1v = cs3.capacitiveSensor(80);
    if (cs3_1v > 1000 && cs3_2v < 1500){
      lick3++;
    }
  } else {
    cs3_2v = cs3.capacitiveSensor(80);
    if (cs3_2v > 1000 && cs3_1v < 1500){
      lick3++;
    }
  }

  // print the lick and timestamp values to the serial port
  Serial.print(lick1);
  Serial.print(":");
  Serial.print(lick2);
  Serial.print(":");
  Serial.print(lick3);
  Serial.print("\n");
  delay(20);
  loopCount++;
}
