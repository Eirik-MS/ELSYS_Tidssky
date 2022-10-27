//Knapp Sketch
#include <FastLED.h> 
#define LED_PIN  13                       
#define NUM_LEDS 45
#define LED_TYPE NEOPIXEL
#define MIN_BRIGHTNESS 240                   
#define MAX_BRIGHTNESS 255        
           
struct CRGB leds[NUM_LEDS];
const int buttonPin = 2;     
int buttonState = 0;        
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
  buttonState = digitalRead(buttonPin);
  Serial.println(buttonState);
  if (buttonState == HIGH) {
    delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) {
      leds[dot] = CRGB(218,51,255);
      FastLED.show();
      delay(10);
      }
    delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) {
      leds[dot] = CRGB(151,17,233);
      FastLED.show();
      delay(10);
      }
    delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) {
      leds[dot] = CRGB(19,141,117);
      FastLED.show();
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
    delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(0,0,0);
            FastLED.show();
            // clear this led for the next time around the loop
            delay(10);
            }
  }
     

}
