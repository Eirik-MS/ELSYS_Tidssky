//Knapp Sketch
 #include <FastLED.h>
 // change these to match your hardware setup
 
#define LED_PIN 7                         // hardware SPI pin SCK
#define NUM_LEDS 45
#define LED_TYPE NEOPIXEL
#define MIN_BRIGHTNESS 240                   // watch the power!
#define MAX_BRIGHTNESS 255                   // watch the power!

struct CRGB leds[NUM_LEDS];


// constants won't change. They're used here to
// set pin numbers:
const int buttonPin = 2;     // the number of the pushbutton pin
// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status
void setup() {
  LEDS.addLeds<LED_TYPE, LED_PIN>(leds, NUM_LEDS);
  FastLED.setBrightness(MAX_BRIGHTNESS);
  FastLED.clear();
  Serial.begin(9600);
  // initialize the LED pin as an output:
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}
int hue = 0;
int divisor = 30;
void loop() {
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);
  // Show the state of pushbutton on serial monitor
  Serial.println(buttonState);
  // check if the pushbutton is pressed.
  // if it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    float breath = (exp(sin(millis()/50.0*PI)) - 0.36787944)*108.0;
    breath = map(breath, 0, 255, MIN_BRIGHTNESS, MAX_BRIGHTNESS);
    FastLED.setBrightness(breath);
    delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) {
      leds[dot] = CRGB(218,51,255);
      FastLED.show();
      // clear this led for the next time around the loop
      delay(10);
      }
      delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
       leds[dot] = CRGB(151,17,233);
       FastLED.show();
         // clear this led for the next time around the loop
       delay(10);
      }

        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) {
      leds[dot] = CRGB(19,141,117);
      FastLED.show();
            // clear this led for the next time around the loop
      delay(10);
          }
  
          delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(17,233,223);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }
        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(218,51,255);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }
        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
          leds[dot] = CRGB(151,17,233);
          FastLED.show();
          // clear this led for the next time around the loop
          delay(10);
        }

        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
          leds[dot] = CRGB(19,141,117);
          FastLED.show();
          // clear this led for the next time around the loop
          delay(10);
          }
  
          delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(17,233,223);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(218,51,255);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }
        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(151,17,233);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }

        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(19,141,117);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
          }
  
          delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(17,233,223);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }
        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(218,51,255);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }
        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(151,17,233);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }

        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(19,141,117);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
          }
  
          delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(17,233,223);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }

        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB::Black;
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }
        delay(2000);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,100,0);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        } delay(10);
        
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,128,0);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }


        delay(1000);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(202,102,0);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
          }
  
        delay(1000);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,120,0);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }
        delay(2000);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,100,0);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        } delay(10);
        
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,128,0);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }


        delay(1000);
     for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(202,102,0);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
          }
  
        delay(1000);
     for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,120,0);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }
        for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB::Black;
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }
        delay(2000);
  delay(100);
        for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB::Black;
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }
        delay(100);
        for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,20,100);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        } delay(10);
        
        for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(245,0,138);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }


        delay(100);
        for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,0,107);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
          }
  
        delay(100);
        for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,0,100);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }
        delay(100);
        for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,20,100);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        } delay(10);
        
        for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(245,0,138);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }


        delay(100);
        for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,0,107);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
          }
  
        delay(100);
        for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,0,100);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }
        for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB::Black;
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }
        delay(2000);

  } else {
    // turn LED off:
              delay(100);
        for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(0,0,0);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
        }
  }
  // Added the delay so that we can see the output of button
  delay(100);
}
