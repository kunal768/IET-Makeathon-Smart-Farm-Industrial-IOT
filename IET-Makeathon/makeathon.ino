//LDR
int ldrPin = A0;
int ldrValue = 0;

//moisture
int sensor_pin = A1;
int output_value;

//flame
int sensorPin = A3; // select the input pin for the LDR
int sensorValue = 0;

//temp and humidity
#include<dht.h>
dht DHT;
#define DHT11_PIN 2

int arr[5]={0,0,0,0,0};

#include<string.h>

void setup()
{
    Serial.begin(9600);
}

void loop()
{
  //LDR
  ldrValue = analogRead(ldrPin);
  arr[0]=ldrValue;
  
  //moisture
  output_value= analogRead(sensor_pin);
  output_value = map(output_value,550,0,0,100);
  arr[1]=output_value+70;

  //rain
  int value = analogRead(A2);
  arr[2]=value;
  //Serial.println(value);
  

  //flame
  sensorValue = analogRead(sensorPin);
  arr[3]=sensorValue;

  //temp and humidity
  int chk = DHT.read11(DHT11_PIN);
  char temp[3];
  char humid[5];

  char ldr[4];
  char moist[4];
  char rain[4];
  char flame[4];

  itoa(arr[0], ldr, 10);
  itoa(arr[1], moist, 10);
  itoa(arr[2], rain, 10);
  itoa(arr[3], flame, 10);
  itoa(DHT.temperature, temp, 10);
  itoa(DHT.humidity, humid, 10);

  
  //Serial.print(ldr);
  //Serial.print(",");
  Serial.print(moist);
  Serial.print(",");
  Serial.print(rain);
  Serial.print(",");
  if (value > 400)
  {
    Serial.print("Very heavy Rain,");
  }
  else if ((value > 125) && (value <= 400))
  {
    Serial.print("AVERAGE Rain,");
  }
  else
  {
    Serial.print("Dry Weather,");
  }
  Serial.print(flame);
  Serial.print(",");
  Serial.print(temp);
  Serial.print(",");
  Serial.println(humid);

  //Serial.println(arr);   //[LDR, Moisture, rain, flame, temp, humidity]
  delay(1000);
}
