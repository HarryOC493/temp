// Pot Mappings. Format VMax | VMin | AMax | AMin | PIN | PrevPosition | Prev Time
// L_Thigh
float L_Thigh[7] = {1.86, 0.50, 60, -90, A0, 0, 0};
// R_Thigh
float R_Thigh[7] = {2.65, 0.56, 90, -90, A3, 0, 0};

// L_Knee
float L_Knee[7] = {3.30, 2.00, 10, -90, A1, 0, 0};
// R_Knee
float R_Knee[7] = {1.94, 0.01, 90, -65, A4, 0, 0};

// L_Ankle
float L_Ankle[7] = {1.51, 0.66, 25, -40, A2, 0, 0};
// R_Ankle
float R_Ankle[7] = {1.33, 1.97, 25, -40, A5, 0, 0};

void setup() {
  Serial.begin(9600); // Initialize serial communication for debugging
  // Print the table header
  Serial.println("Joint\tVMax\tVMin\tVoltage");
}

float Read_Angle(float joint[7]) {
  int sensorValue = analogRead((int)joint[4]);
  float voltage = sensorValue * (3.3 / 1023.0); // Convert to voltage (0-5V)
  int angle = int(fmap(voltage, joint[1], joint[0], joint[3], joint[2]));

  float deltaTime = (millis() - joint[6]) / 1000.0;
  float deltaAngle = angle - joint[5];
  float velocity = deltaAngle / deltaTime;

  joint[5] = angle;
  joint[6] = millis();

  // Print the angle and velocity to the serial monitor for debugging
  Serial.print("Potentiometer Angle: ");
  Serial.print(angle);
  Serial.print(" degrees        ");
  Serial.print("Velocity: ");
  Serial.print(velocity);
  Serial.print(" degrees/s       ");
  Serial.println(voltage);

  return angle;
}

void printVoltage(float joint[7]) {
  int sensorValue = analogRead((int)joint[4]);
  float voltage = sensorValue * (3.3 / 1023.0);
  Serial.print("A"); Serial.print((int)joint[4]);
  Serial.print("\t");
  Serial.print(joint[0], 2);
  Serial.print("\t");
  Serial.print(joint[1], 2);
  Serial.print("\t");
  Serial.println(voltage, 2);
}

void loop() {
  // Read and print angles and velocities for each joint
  Read_Angle(L_Thigh);
  Read_Angle(R_Thigh);
  Read_Angle(L_Knee);
  Read_Angle(R_Knee);
  Read_Angle(L_Ankle);
  Read_Angle(R_Ankle);

  // Print voltage readings in a table format
  printVoltage(L_Thigh);
  printVoltage(R_Thigh);
  printVoltage(L_Knee);
  printVoltage(R_Knee);
  printVoltage(L_Ankle);
  printVoltage(R_Ankle);

  Serial.println(); // Blank line for readability

  delay(1000); // Delay for a second (adjust as needed)
}

float fmap(float x, float in_min, float in_max, float out_min, float out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
