// Demo code for Grove - Temperature Sensor V1.1/1.2
// Loovee @ 2015-8-26

#include <math.h>

const int B=4275;                 // B value of the thermistor
const int R0 = 100000;            // R0 = 100k
const int pinTempSensor = A0;     // Grove - Temperature Sensor connect to A0

#define LIGHT_SENSOR A1//Grove - Light Sensor is connected to A0 of Arduino
const int thresholdvalue=10;         //The treshold for which the LED should turn on. Setting it lower will make it go on at more light, higher for more darkness
float Rsensor; //Resistance of sensor in K

#include <Wire.h>
#include <Adafruit_MPL3115A2.h>

Adafruit_MPL3115A2 baro = Adafruit_MPL3115A2();

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    int a = analogRead(pinTempSensor );

    float R = 1023.0/((float)a)-1.0;
    R = 100000.0*R;

    float temperature=1.0/(log(R/100000.0)/B+1/298.15)-273.15;    //convert to temperature via datasheet ;

    float pressureVariable = (float)random(6500, 9000) / 100;

    int sensorValue = analogRead(LIGHT_SENSOR); 
    Rsensor = (float)(1023-sensorValue)*10/sensorValue;

//    float pascals = baro.getPressure();
    float pascals = (float)random(10, 50);


    Serial.println(temperature);

    Serial.println(pressureVariable, 2);

//    Serial.println(sensorValue);    //show the ligth intensity on the serial monitor;
    if(sensorValue<100)
        Serial.println("Yes");    
    else
        Serial.println("No");

    if(pascals*0.10197162129779/25.13<0.5)
        Serial.println("Yes");    
    else
        Serial.println("No");
        

    Serial.flush();

    
    delay(1000);
}
