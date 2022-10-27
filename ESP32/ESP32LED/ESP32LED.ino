 #include <FastLED.h>
  // change these to match your hardware setup

#define LED_PIN 7                         // hardware SPI pin SCK
#define NUM_LEDS 45
#define LED_TYPE NEOPIXEL
#define MIN_BRIGHTNESS 8                   // watch the power!
#define MAX_BRIGHTNESS 255                   // watch the power!

struct CRGB leds[NUM_LEDS];

void setup()
{
     LEDS.addLeds<LED_TYPE, LED_PIN>(leds, NUM_LEDS);
     FastLED.setBrightness(MAX_BRIGHTNESS);
     FastLED.clear();
}

int hue = 0;
int divisor = 30;
void loop () {
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
  if(hue == (255 * divisor)) {
    hue = 0;
  }
  FastLED.show();
  delay(5);
  breath = map(breath, 0, 255, MIN_BRIGHTNESS, MAX_BRIGHTNESS);
  FastLED.setBrightness(breath);
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

}
