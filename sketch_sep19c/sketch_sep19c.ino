#include <SoftwareSerial.h>
#include <AFMotor.h>

AF_DCMotor motor_L(1);
AF_DCMotor motor_R(4);

int i;

int TrigPin = A0;
int EchoPin = A1;
int duration, distance;

void Obstacle_Check();
void Distance_Measurement();
void Forward();
void Backward();
void Right();
void Left();
void Stop();


void Obstacle_Check(){
 int val = random(2);
 Distance_Measurement();

 Serial.println(distance);

 while (distance < 200) {
  if (distance<180) {
    Backward();
    delay(250);
    Stop();
    delay(50);
    Distance_Measurement();
  }
  else {
    if (val == 0){
      Right ();
      delay(400);
    }
    else if (val == 1) {
      Left ();
      delay(400);
    }
    Distance_Measurement();
  }
 }
}
void Distance_Measurement(){
  digitalWrite(TrigPin, LOW);
  delay(2);
  digitalWrite(TrigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(TrigPin, LOW);
  duration = pulseIn(EchoPin, HIGH);
  distance = ((float)(340 * duration) / 1000) /2;
  delay(5);
}

void Backward(){
  motor_L.run(FORWARD); motor_R.run(FORWARD);
  for (i = 0; i<200; i = i+20) {
    motor_L.setSpeed(i); motor_R.setSpeed(i);
    delay(2);
  }
  for( i = 200; i<0; i = i-20) {
    motor_L.setSpeed(i); motor_R.setSpeed(i);
    delay(2);
  }
}

void Forward (){
  motor_L.run(BACKWARD); motor_R.run(BACKWARD);
  for (i = 0; i<200; i = i+20) {
    motor_L.setSpeed(i); motor_R.setSpeed(i);
    delay(2);
  }
  for( i = 200; i<0; i = i-20) {
    motor_L.setSpeed(i); motor_R.setSpeed(i);
    delay(2);
}
}
void Right(){
  motor_L.run(FORWARD); motor_R.run(BACKWARD);
  for( i=0; i<180; i = i+20){
    motor_L.setSpeed(i); motor_R.setSpeed(i);
    delay(2);
  }
  for(i=180; i<0; i = i-20){
    motor_L.setSpeed(i); motor_R.setSpeed(i);
    delay(2);
  }
}
void Left(){
  motor_L.run(BACKWARD); motor_R.run(FORWARD);
  for( i=0; i<180; i = i+20){
    motor_L.setSpeed(i); motor_R.setSpeed(i);
    delay(2);
  }
  for(i=180; i<0; i = i-20){
    motor_L.setSpeed(i); motor_R.setSpeed(i);
    delay(2);
  }
}
void Stop(){
  motor_L.run(RELEASE); motor_R.run(RELEASE);
  for(i=200; i>=0; i=i-20){
    motor_L.setSpeed(i); motor_R.setSpeed(i);
    delay(2);
  }
}

void setup() {
Serial.begin(9600);
Serial.println("Eduino Smart Car Start!");

pinMode(EchoPin, INPUT);
pinMode(TrigPin, OUTPUT);

motor_L.setSpeed(160);
motor_L.run(RELEASE);
motor_R.setSpeed(180);
motor_R.run(RELEASE);
}

void loop() {
  Forward();
  delay(100);
  Obstacle_Check();
}
