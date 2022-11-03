//Knapp Sketch
#include <FastLED.h>  // Inkluderer biblioteket vi trenger
#define LED_PIN  13                       // Setter pin for rgb-strip til 13
#define NUM_LEDS 45 // Setter antall dioder på listen til 45
#define LED_TYPE NEOPIXEL // Setter pixeltype
#define MIN_BRIGHTNESS 240                   // Lysstyrke for lightstrip
#define MAX_BRIGHTNESS 255        
           
struct CRGB leds[NUM_LEDS]; // CRGB skal endre antall LEDs
const int buttonPin = 2;     // Setter buttonpin som en konstant 2
int buttonState = 0;         // Setter startverdi til button som 0
void setup() {
  LEDS.addLeds<LED_TYPE, LED_PIN>(leds, NUM_LEDS); // Definerer antall leds
  FastLED.setBrightness(MAX_BRIGHTNESS); // Setter lysstyrke
  FastLED.clear(); // Tømmer led-strip
  Serial.begin(9600);
  pinMode(buttonPin, INPUT); // Setter button som input
}
int hue = 0;
int divisor = 30;
void loop() {
  buttonState = digitalRead(buttonPin);
  Serial.println(buttonState);
  if (buttonState == HIGH) {                 // Kjører loopen dersom button er trykket inn
    delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { // For løkke som endrer en og en LED til fargen oppgitt
      leds[dot] = CRGB(218,51,255); // Setter farge
      FastLED.show(); // viser farge
      delay(10); // senker ned hastigheten diodene endrer farge i 
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
            delay(10);
        }
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
            delay(10);
        }
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
            delay(10);
        }
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
            delay(10);
        }

        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB::Black;
            FastLED.show();
            delay(10);
        }
        delay(2000);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,100,0);
            FastLED.show();
            delay(10);
        } delay(10);
        
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,128,0);
            FastLED.show();
            delay(10);
        }


        delay(1000);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(202,102,0);
            FastLED.show();
            delay(10);
          }
  
        delay(1000);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,120,0);
            FastLED.show();
            delay(10);
        }
        delay(2000);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,100,0);
            FastLED.show();
            delay(10);
        } delay(10);
        
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,128,0);
            FastLED.show();
            delay(10);
        }


        delay(1000);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(202,102,0);
            FastLED.show();
            delay(10);
          }
  
        delay(1000);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,120,0);
            FastLED.show();
            delay(10);
        }
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB::Black;
            FastLED.show();
            delay(10);
        }
        delay(2000);
        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB::Black;
            FastLED.show();
            delay(10);
        }
        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,20,100);
            FastLED.show();
            delay(10);
        } delay(10);
        
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(245,0,138);
            FastLED.show();
            delay(10);
        }


        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,0,107);
            FastLED.show();
            delay(10);
          }
  
        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,0,100);
            FastLED.show();
            delay(10);
        }
        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,20,100);
            FastLED.show();
            delay(10);
        } delay(10);
        
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(245,0,138);
            FastLED.show();
            delay(10);
        }


        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,0,107);
            FastLED.show();
            delay(10);
          }
  
        delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(255,0,100);
            FastLED.show();
            delay(10);
        }
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB::Black;
            FastLED.show();
            delay(10);
            }
        delay(2000);
  } else {                                    // Else står i forhold til om knappen er trykket, så dersom knappen er 0, vil alle diodene endre til svart.
    delay(100);
    for(int dot = 0; dot < NUM_LEDS; dot++) { 
            leds[dot] = CRGB(0,0,0);
            FastLED.show();
            delay(10);
            }
  }
     

}
