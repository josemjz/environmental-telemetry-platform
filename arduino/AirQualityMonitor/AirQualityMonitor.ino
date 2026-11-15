#include "arduino_secrets.h"
/*
NEW SKETCH

NEW SKETCH

  Purple Air Arduino Reader

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include <ArduinoGraphics.h> // Arduino_MKRRGB depends on ArduinoGraphics
#include <Arduino_MKRRGB.h>
#include <WiFiNINA.h>
#include <ArduinoHttpClient.h>
#include <Arduino_JSON.h>

// Air quality level PM2.5 μg/m3  (see https://blissair.com/what-is-pm-2-5.htm)
int max_level[] = {12, 35, 55, 150, 250, 500};
String labels[] = {"Good", "Moderate", "USG", "Unhealthy", "V Unhealthy", "Hazardous"};
int color[][3] = {{0, 255, 0}, {255, 255, 0}, {255, 128, 0}, {255, 0, 0}, {128, 0, 128}, {128, 0, 0}};

long timer = 0;

// please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;  // your network SSID (name)
char pass[] = SECRET_PASS;  // your network password
String sensor_id = SECRET_SENSOR_ID;

int status = WL_IDLE_STATUS;
char server[] = "www.purpleair.com";
WiFiClient wifi;
HttpClient client = HttpClient(wifi, server, 80);
int port = 8080;

void setup() {

  Serial.begin(9600);

  while ( status != WL_CONNECTED) {
    Serial.print("Attempting to connect to Network named: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid, pass);
  }
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your WiFi shield's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  MATRIX.begin();
  MATRIX.brightness(2);
  MATRIX.textScrollSpeed(50);
}

void loop() {
  getAirQuality();
  delay(20000);
}

void getAirQuality() {
  Serial.println("Requesting data from PurpleAir");
  client.get("/json?show=" + sensor_id);
  int statusCode = client.responseStatusCode();

  if (statusCode == 302 || statusCode == 303) {
    String location;
    Serial.println("Redirection");
    while (client.headerAvailable()) {
        if (client.readHeaderName() == "Location") {
            location = client.readHeaderValue();
            break;
        }
    }
    if (location.length()) {
        uint16_t path_begin = location.substring(8).indexOf('/');
        String server = location.substring(8, path_begin + 8);
        String path = location.substring(path_begin + 8);

        // Reset the existing client
        
        client = HttpClient(wifi, server, port);

        // Make a new request to the redirected location
        client.get(path);
        statusCode = client.responseStatusCode();
        
        Serial.print("Status code after redirect is: ");
        Serial.println(statusCode);

        if (statusCode == -2) {
            Serial.println("Error during redirection. Connection error code: ");
        }
    }
}


  String response = client.responseBody();
  Serial.println(statusCode);
  Serial.println(response);

  int level = 5;
  JSONVar myObject = JSON.parse(response);
  int PM2_5 = atoi(myObject["results"][0]["PM2_5Value"]);
  Serial.println(PM2_5);
  Serial.println(JSON.typeof(myObject));
  // JSON.stringify(myVar) can be used to convert the JSONVar to a String
  String jsonString = JSON.stringify(myObject);

  Serial.print("JSON.stringify(myObject) = ");
  Serial.println(jsonString);

  if (statusCode == 200) {
    JSONVar myObject = JSON.parse(response);
    int PM2_5 = atoi(myObject["results"][0]["PM2_5Value"]);
    Serial.println(PM2_5);

    // Find air quality level
    for (int i = 0; i < 6; i++) {
      if (PM2_5 <= max_level[i]) {
        level = i;
        break;
      }
    }

    Serial.println(PM2_5);
    Serial.println(labels[level]);

    timer = millis();

    MATRIX.beginText(MATRIX.width() - 1, 0, color[level][0], color[level][1], color[level][2]); // X, Y, then R, G, B
    MATRIX.print(PM2_5);
    MATRIX.print("  ");
    MATRIX.println(labels[level]);
    MATRIX.endText(SCROLL_LEFT);

    MATRIX.beginDraw();
    MATRIX.stroke(color[level][0], color[level][1], color[level][2]);
    MATRIX.rect(0, 0, MATRIX.width(),  MATRIX.height());
    MATRIX.endDraw();

  }
}
