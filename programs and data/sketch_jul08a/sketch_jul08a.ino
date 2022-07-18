
#include <WiFi.h>


char ssid[] = "SATYAJIT";   // your network SSID (name) 
char pass[] = "satyajit";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  WiFi.begin(ssid, pass);
  Serial.println("connecting to wifi");

  while(WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(500);
  }

  Serial.println("\n connected to wifi");
  Serial.println(WiFi.localIP());
}

void loop() {
  // put your main code here, to run repeatedly:

}
