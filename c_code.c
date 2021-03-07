#include <Servo.h>
#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

Servo servoBase;
Servo servoArmFirst;
Servo servoArmSecond;
Servo servoArmThirdPullString;
Servo servoArmFourth;
Servo mechanicalArm;


bool isOpen;

char* baseMove;
char* armOne;
char* armTwo;
char* armThree;
char* armFour;
char* mechanical;
char* json;

int angleBase, angleArmOne, angleArmTwo, angleArmThree, angleArmFour = 1;
int distanceForAngle = 0;
int currentAngle = 0;
int microseconds;
int formatedData;
int pullAngle;
int angleofbase = 0;
int currentangle = 0;

const int echoPin = 11;
const int trigPin = 12;

const char* ssid = "Singhome";
const char* passwordwifi = "Nicolas02";

void setup() {
  Serial.begin(9600);
  //assigning servos
  servoBase.attach(5);
  servoArmFirst.attach(6);
  servoArmSecond.attach(7);
  servoArmThirdPullString.attach(8);
  servoArmFourth.attach(9);
  mechanicalArm.attach(10);
 
  // Wifi name and pass
  //if(Serial.available()<0){
  //  ssid = Serial.read();
  //  Serial.flush();
  //  password = Serial.read();
  //  Serial.flush();
  //  Serial.print("Wifi Name: ");
  //  Serial.println(ssid);
  //  Serial.print("Password: ");
  //  Serial.println(password);
  //  delay(3000);
  //  Serial.flush();

  WiFi.begin(ssid, passwordwifi);
 
  while (WiFi.status() != WL_CONNECTED) {
 
    delay(1000);
    Serial.println("Connecting..");
 
  }
  Serial.println("Connected to WiFi Network");
 
}

void loop() {
  connectWifi();
  delay(1000);
  readJSONdict();
}

// Functions
void connectWifi(){
  if (WiFi.status() == WL_CONNECTED) {
 
    HTTPClient http;
    http.begin("http://www.nicolasryjoukhine.pythonanywhere.com/send-to-arduino");
    int httpCode = http.GET();
    if (httpCode > 0) {
      String payload = http.getString();
      Serial.println(payload);
      //json = Serial.readStringUntil("\n");
      json = payload;
    }else Serial.println("An error ocurred");
    http.end();
  }
}

void readJSONdict() {
  StaticJsonDocument<200> commandsList;
  deserializeJson(commandsList, json);

  baseMove = commandsList["bottomServoAction"];
  armOne = commandsList["firstArmPistonAction"];
  armTwo = commandsList["secondArmPistonAction"];
  armThree = commandsList["thirdArmServoPullBackString"];
  armFour = commandsList["fourthArmPistonAction"];
  mechanical = commandsList["gripperArmAction"];
  Serial.print(baseMove);
  if(baseMove == "BASE_MOVE_RIGHT\n"){
    Serial.print("ASASAS");
    angleBase++;
  } else {
    angleBase--;
  }
 
  if(armOne != "ActionHere"){
    if(armOne == "PULL_UP"){
      angleArmOne++;
    } else {
      angleArmOne--;
    }
  }
  if(armTwo != "ActionHere"){
    if(armTwo == "PULL_UP"){
      angleArmTwo++;
    } else {
      angleArmTwo--;
    }
  }
  if(armThree != "ActionHere"){
    if(armThree == "PULL_UP"){
      angleArmThree++;
    } else {
      angleArmThree--;
    }
  }
  if(armFour != "ActionHere"){
    if(armFour == "PULL_UP"){
      angleArmFour++;
    } else {
      angleArmFour--;
    }
  }
  if(mechanical != "ActionHere"){
    if(mechanical == "OPEN"){
      isOpen = true;
    } else {
      isOpen = false;
    }
  }
  //Serial.print(angleBase, angleBase,angleArmOne,angleArmTwo,angleArmThree,angleArmFour,
  //              isOpen,baseMove,armOne,armTwo,armThree,armFour,mechanical);
  rotateBase(angleBase);
  armOnemove(angleArmOne);
  armTwomove(angleArmTwo);
  armThreemove(angleArmThree);
  armMoveFourth(angleArmFour);
  grabberArm(isOpen);
}


void readDataDistance() {
  pinMode(trigPin, OUTPUT);
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(2);
  digitalWrite(trigPin, LOW);
  microseconds = pulseIn(echoPin, HIGH);
  formatedData = microseconds / 29 / 2;
  Serial.println(formatedData);
}



// Servo actions

void rotateBase(int angle) {
  if (angle < 180) {
    servoBase.write(angle);
  }
}
void armOnemove(int angle) {
  if(angle < 115){
    servoArmFirst.write(angle);
  }
}
void armTwomove(int angle) {
  if(angle < 115){
    servoArmSecond.write(angle);
  }
}
void armThreemove(int angle) {
  if(angle < 115){
    pullAngle = angle / 180 / 18.9 * 3;
    servoArmThirdPullString.write(pullAngle);
  }
}
void armMoveFourth(int angle) {
  if (angle > 90 and angle < 180) {
    servoArmFourth.write(angle);
  }
}
void grabberArm(bool isOpen) {
  if(isOpen == true){
    mechanicalArm.write(60);
  } else {
    mechanicalArm.write(0);
  }
}
