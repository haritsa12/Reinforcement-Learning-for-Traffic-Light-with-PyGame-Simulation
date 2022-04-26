#include <FastLED.h>

#define LED_PIN_W     A2
#define LED_PIN_N     A3
#define LED_PIN_E     A4
#define LED_PIN_S     A5

#define NUM_leds_W    12
#define NUM_leds_N    15
#define NUM_leds_E    15
#define NUM_leds_S    15


CRGB leds_W[NUM_leds_W];
CRGB leds_N[NUM_leds_N];
CRGB leds_E[NUM_leds_E];
CRGB leds_S[NUM_leds_S];

String incomingByte ;    
int west,north,east,south,byte_to_int,byte_to_int_action;
void setup() {

  Serial.begin(9600);

  pinMode(LED_BUILTIN, OUTPUT);
  FastLED.addLeds<WS2812, LED_PIN_W, GRB>(leds_W, NUM_leds_W);
  FastLED.addLeds<WS2812, LED_PIN_N, GRB>(leds_N, NUM_leds_N);
  FastLED.addLeds<WS2812, LED_PIN_E, GRB>(leds_E, NUM_leds_E);
  FastLED.addLeds<WS2812, LED_PIN_S, GRB>(leds_S, NUM_leds_S);
  FastLED.setBrightness(  4 );
  pinMode(8, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  
}
void loop() {

  if (Serial.available() > 0) {

  incomingByte = Serial.readStringUntil('\n');
  byte_to_int_action=incomingByte.toInt();

  if (byte_to_int_action==100){
    digitalWrite(LED_BUILTIN, HIGH);
    digitalWrite(7, LOW); 
    digitalWrite(6, LOW);
    digitalWrite(5, HIGH); 
    
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW); 
    digitalWrite(4, LOW);
    
    digitalWrite(8, HIGH); 
    digitalWrite(10, LOW);
    digitalWrite(9, LOW);
    
    digitalWrite(12, HIGH);
    digitalWrite(11, LOW);
    digitalWrite(13, LOW);
    //delay(500);
  }

  else if (byte_to_int_action==101){
    digitalWrite(7, HIGH); 
    digitalWrite(6, LOW);
    digitalWrite(5, LOW); 
    
    digitalWrite(2, LOW);
    digitalWrite(3, LOW); 
    digitalWrite(4, HIGH);
    
    digitalWrite(8, HIGH); 
    digitalWrite(10, LOW);
    digitalWrite(9, LOW);
    
    digitalWrite(12, HIGH);
    digitalWrite(11, LOW);
    digitalWrite(13, LOW);
//    delay(500);
  }

  else if (byte_to_int_action==102){
    digitalWrite(7, HIGH); 
    digitalWrite(6, LOW);
    digitalWrite(5, LOW); 
    
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW); 
    digitalWrite(4, LOW);
    
    digitalWrite(8, LOW); 
    digitalWrite(10, LOW);
    digitalWrite(9, HIGH);
    
    digitalWrite(12, HIGH);
    digitalWrite(11, LOW);
    digitalWrite(13, LOW);
//    delay(500);
  }

  else if (byte_to_int_action==103){
    digitalWrite(7, HIGH); 
    digitalWrite(6, LOW);
    digitalWrite(5, LOW); 
    
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW); 
    digitalWrite(4, LOW);
    
    digitalWrite(8, HIGH); 
    digitalWrite(10, LOW);
    digitalWrite(9, LOW);
    
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
    digitalWrite(13, HIGH);
//    delay(500);
  }
    
  
  byte_to_int=incomingByte.toInt();
    west=byte_to_int/27;
    north=(byte_to_int%27)/9;
    east=((byte_to_int%27)%9)/3;
    south=(((byte_to_int%27)%9)%3);
    if (west == 0) {

      digitalWrite(LED_BUILTIN, HIGH);
      leds_W[0] = CRGB(255, 0, 0);
      FastLED.show();
      leds_W[1] = CRGB(255, 0, 0);
      FastLED.show();
      leds_W[2] = CRGB(255, 0, 0);
      FastLED.show();
      leds_W[3] = CRGB(255, 0, 0);
      FastLED.show();
      leds_W[4] = CRGB(0, 0, 0);
      FastLED.show();
      leds_W[5] = CRGB(0, 0, 0);
      FastLED.show();
      leds_W[6] = CRGB(0, 0, 0);
      FastLED.show();
      leds_W[7] = CRGB(0, 0, 0);
      FastLED.show();
      leds_W[8] = CRGB(0, 0, 0);
      FastLED.show();
      leds_W[9] = CRGB(0, 0, 0);
      FastLED.show();
      leds_W[10] = CRGB(0, 0, 0);
      FastLED.show();
      leds_W[11] = CRGB(0, 0, 0);
      FastLED.show();
      delay(500);  
      Serial.write("Led on");

    }

    else if (west==1){

      digitalWrite(LED_BUILTIN, HIGH);
      leds_W[0] = CRGB(0, 255, 0);
      FastLED.show();
      leds_W[1] = CRGB(0, 255, 0);
      FastLED.show();
      leds_W[2] = CRGB(0, 255, 0);
      FastLED.show();
      leds_W[3] = CRGB(0, 255, 0);
      FastLED.show();
      leds_W[4] = CRGB(0, 255, 0);
      FastLED.show();
      leds_W[5] = CRGB(0, 255, 0);
      FastLED.show();
      leds_W[6] = CRGB(0, 255, 0);
      FastLED.show();
      leds_W[7] = CRGB(0, 0, 0);
      FastLED.show();
      leds_W[8] = CRGB(0, 0, 0);
      FastLED.show();
      leds_W[9] = CRGB(0, 0, 0);
      FastLED.show();
      leds_W[10] = CRGB(0, 0, 0);
      FastLED.show();
      leds_W[11] = CRGB(0, 0, 0);
      FastLED.show();
      delay(500);  
      Serial.write("Led on");      
    }

    else if (west == 2) {

      digitalWrite(LED_BUILTIN, LOW);
      leds_W[0] = CRGB(0, 0, 255);
      FastLED.show();
      leds_W[1] = CRGB(0, 0, 255);
      FastLED.show();
      leds_W[2] = CRGB(0, 0, 255);
      FastLED.show();
      leds_W[3] = CRGB(0, 0, 255);
      FastLED.show(); 
      Serial.write("Led on");
      leds_W[4] = CRGB(0, 0, 255);
      FastLED.show();
      leds_W[5] = CRGB(0, 0, 255);
      FastLED.show();
      leds_W[6] = CRGB(0, 0, 255);
      FastLED.show();
      leds_W[7] = CRGB(0, 0, 255);
      FastLED.show();
      leds_W[8] = CRGB(0, 0, 255);
      FastLED.show();
      leds_W[9] = CRGB(0, 0, 255);
      FastLED.show();
      leds_W[10] = CRGB(0, 0, 255);
      FastLED.show();
      leds_W[11] = CRGB(0, 0, 255);
      FastLED.show();
      delay(500);
      Serial.write("Led off");

    }

    if (north== 0) {

      digitalWrite(LED_BUILTIN, HIGH);
      leds_N[0] = CRGB(255, 0, 0);
      FastLED.show();
      leds_N[1] = CRGB(255, 0, 0);
      FastLED.show();
      leds_N[2] = CRGB(255, 0, 0);
      FastLED.show();
      leds_N[3] = CRGB(255, 0, 0);
      FastLED.show();
      leds_N[4] = CRGB(0, 0, 0);
      FastLED.show();
      leds_N[5] = CRGB(0, 0, 0);
      FastLED.show();
      leds_N[6] = CRGB(0, 0, 0);
      FastLED.show();
      leds_N[7] = CRGB(0, 0, 0);
      FastLED.show();
      leds_N[8] = CRGB(0, 0, 0);
      FastLED.show();
      leds_N[9] = CRGB(0, 0, 0);
      FastLED.show();
      leds_N[10] = CRGB(0, 0, 0);
      FastLED.show();
      leds_N[11] = CRGB(0, 0, 0);
      FastLED.show();
      delay(500);  
      Serial.write("Led on");

    }

    else if (north==1){

      digitalWrite(LED_BUILTIN, HIGH);
      leds_N[0] = CRGB(0, 255, 0);
      FastLED.show();
      leds_N[1] = CRGB(0, 255, 0);
      FastLED.show();
      leds_N[2] = CRGB(0, 255, 0);
      FastLED.show();
      leds_N[3] = CRGB(0, 255, 0);
      FastLED.show();
      leds_N[4] = CRGB(0, 255, 0);
      FastLED.show();
      leds_N[5] = CRGB(0, 255, 0);
      FastLED.show();
      leds_N[6] = CRGB(0, 255, 0);
      FastLED.show();
      leds_N[7] = CRGB(0, 0, 0);
      FastLED.show();
      leds_N[8] = CRGB(0, 0, 0);
      FastLED.show();
      leds_N[9] = CRGB(0, 0, 0);
      FastLED.show();
      leds_N[10] = CRGB(0, 0, 0);
      FastLED.show();
      leds_N[11] = CRGB(0, 0, 0);
      FastLED.show();
      delay(500);  
      Serial.write("Led on");      
    }

    else if (north == 2) {

      digitalWrite(LED_BUILTIN, LOW);
      leds_N[0] = CRGB(0, 0, 255);
      FastLED.show();
      leds_N[1] = CRGB(0, 0, 255);
      FastLED.show();
      leds_N[2] = CRGB(0, 0, 255);
      FastLED.show();
      leds_N[3] = CRGB(0, 0, 255);
      FastLED.show(); 
      Serial.write("Led on");
      leds_N[4] = CRGB(0, 0, 255);
      FastLED.show();
      leds_N[5] = CRGB(0, 0, 255);
      FastLED.show();
      leds_N[6] = CRGB(0, 0, 255);
      FastLED.show();
      leds_N[7] = CRGB(0, 0, 255);
      FastLED.show();
      leds_N[8] = CRGB(0, 0, 255);
      FastLED.show();
      leds_N[9] = CRGB(0, 0, 255);
      FastLED.show();
      leds_N[10] = CRGB(0, 0, 255);
      FastLED.show();
      leds_N[11] = CRGB(0, 0, 255);
      FastLED.show();
      delay(500);
      Serial.write("Led off");

    }
    
    if (east== 0) {

      digitalWrite(LED_BUILTIN, HIGH);
      leds_E[0] = CRGB(255, 0, 0);
      FastLED.show();
      leds_E[1] = CRGB(255, 0, 0);
      FastLED.show();
      leds_E[2] = CRGB(255, 0, 0);
      FastLED.show();
      leds_E[3] = CRGB(255, 0, 0);
      FastLED.show();
      leds_E[4] = CRGB(0, 0, 0);
      FastLED.show();
      leds_E[5] = CRGB(0, 0, 0);
      FastLED.show();
      leds_E[6] = CRGB(0, 0, 0);
      FastLED.show();
      leds_E[7] = CRGB(0, 0, 0);
      FastLED.show();
      leds_E[8] = CRGB(0, 0, 0);
      FastLED.show();
      leds_E[9] = CRGB(0, 0, 0);
      FastLED.show();
      leds_E[10] = CRGB(0, 0, 0);
      FastLED.show();
      leds_E[11] = CRGB(0, 0, 0);
      FastLED.show();
      delay(500);  
      Serial.write("Led on");

    }

    else if (east==1){

      digitalWrite(LED_BUILTIN, HIGH);
      leds_E[0] = CRGB(0, 255, 0);
      FastLED.show();
      leds_E[1] = CRGB(0, 255, 0);
      FastLED.show();
      leds_E[2] = CRGB(0, 255, 0);
      FastLED.show();
      leds_E[3] = CRGB(0, 255, 0);
      FastLED.show();
      leds_E[4] = CRGB(0, 255, 0);
      FastLED.show();
      leds_E[5] = CRGB(0, 255, 0);
      FastLED.show();
      leds_E[6] = CRGB(0, 255, 0);
      FastLED.show();
      leds_E[7] = CRGB(0, 0, 0);
      FastLED.show();
      leds_E[8] = CRGB(0, 0, 0);
      FastLED.show();
      leds_E[9] = CRGB(0, 0, 0);
      FastLED.show();
      leds_E[10] = CRGB(0, 0, 0);
      FastLED.show();
      leds_E[11] = CRGB(0, 0, 0);
      FastLED.show();
      delay(500);  
      Serial.write("Led on");      
    }

    else if (east == 2) {

      digitalWrite(LED_BUILTIN, LOW);
      leds_E[0] = CRGB(0, 0, 255);
      FastLED.show();
      leds_E[1] = CRGB(0, 0, 255);
      FastLED.show();
      leds_E[2] = CRGB(0, 0, 255);
      FastLED.show();
      leds_E[3] = CRGB(0, 0, 255);
      FastLED.show(); 
      Serial.write("Led on");
      leds_E[4] = CRGB(0, 0, 255);
      FastLED.show();
      leds_E[5] = CRGB(0, 0, 255);
      FastLED.show();
      leds_E[6] = CRGB(0, 0, 255);
      FastLED.show();
      leds_E[7] = CRGB(0, 0, 255);
      FastLED.show();
      leds_E[8] = CRGB(0, 0, 255);
      FastLED.show();
      leds_E[9] = CRGB(0, 0, 255);
      FastLED.show();
      leds_E[10] = CRGB(0, 0, 255);
      FastLED.show();
      leds_E[11] = CRGB(0, 0, 255);
      FastLED.show();
      delay(500);
      Serial.write("Led off");

    }

    if (south== 0) {

      digitalWrite(LED_BUILTIN, HIGH);
      leds_S[0] = CRGB(255, 0, 0);
      FastLED.show();
      leds_S[1] = CRGB(255, 0, 0);
      FastLED.show();
      leds_S[2] = CRGB(255, 0, 0);
      FastLED.show();
      leds_S[3] = CRGB(255, 0, 0);
      FastLED.show();
      leds_S[4] = CRGB(0, 0, 0);
      FastLED.show();
      leds_S[5] = CRGB(0, 0, 0);
      FastLED.show();
      leds_S[6] = CRGB(0, 0, 0);
      FastLED.show();
      leds_S[7] = CRGB(0, 0, 0);
      FastLED.show();
      leds_S[8] = CRGB(0, 0, 0);
      FastLED.show();
      leds_S[9] = CRGB(0, 0, 0);
      FastLED.show();
      leds_S[10] = CRGB(0, 0, 0);
      FastLED.show();
      leds_S[11] = CRGB(0, 0, 0);
      FastLED.show();
      delay(500);  
      Serial.write("Led on");

    }

    else if (south==1){

      digitalWrite(LED_BUILTIN, HIGH);
      leds_S[0] = CRGB(0, 255, 0);
      FastLED.show();
      leds_S[1] = CRGB(0, 255, 0);
      FastLED.show();
      leds_S[2] = CRGB(0, 255, 0);
      FastLED.show();
      leds_S[3] = CRGB(0, 255, 0);
      FastLED.show();
      leds_S[4] = CRGB(0, 255, 0);
      FastLED.show();
      leds_S[5] = CRGB(0, 255, 0);
      FastLED.show();
      leds_S[6] = CRGB(0, 255, 0);
      FastLED.show();
      leds_S[7] = CRGB(0, 0, 0);
      FastLED.show();
      leds_S[8] = CRGB(0, 0, 0);
      FastLED.show();
      leds_S[9] = CRGB(0, 0, 0);
      FastLED.show();
      leds_S[10] = CRGB(0, 0, 0);
      FastLED.show();
      leds_S[11] = CRGB(0, 0, 0);
      FastLED.show();
      delay(500);  
      Serial.write("Led on");      
    }

    else if (south == 2) {

      digitalWrite(LED_BUILTIN, LOW);
      leds_S[0] = CRGB(0, 0, 255);
      FastLED.show();
      leds_S[1] = CRGB(0, 0, 255);
      FastLED.show();
      leds_S[2] = CRGB(0, 0, 255);
      FastLED.show();
      leds_S[3] = CRGB(0, 0, 255);
      FastLED.show(); 
      Serial.write("Led on");
      leds_S[4] = CRGB(0, 0, 255);
      FastLED.show();
      leds_S[5] = CRGB(0, 0, 255);
      FastLED.show();
      leds_S[6] = CRGB(0, 0, 255);
      FastLED.show();
      leds_S[7] = CRGB(0, 0, 255);
      FastLED.show();
      leds_S[8] = CRGB(0, 0, 255);
      FastLED.show();
      leds_S[9] = CRGB(0, 0, 255);
      FastLED.show();
      leds_S[10] = CRGB(0, 0, 255);
      FastLED.show();
      leds_S[11] = CRGB(0, 0, 255);
      FastLED.show();
      delay(500);
      Serial.write("Led off");

    }
    
    

    else{

     Serial.write("invald input");

    }
   
//atas ini batas komen
  }

}


