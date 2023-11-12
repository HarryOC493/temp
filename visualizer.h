// Pot Mappings. Format VMax | VMin | AMax | AMin | PIN | PrevPosition | Prev Time

// L_Thigh
float L_Thigh[7] = {2.54, 0.49, 90, -90, A0, 0, 0};
// L_Knee
float L_Knee[7] = {3.30, 2.00, 10, -90, A1, 0, 0};
// L_Ankle
float L_Ankle[7] = {1.51, 0.66, 25, -40, A2, 0, 0}; // Changed to A2 for correct pin

void setup() {
  Serial.begin(9600);
}

void loop() {
  float angleThigh = Read_Angle(L_Thigh);
  float angleKnee = Read_Angle(L_Knee);
  float angleAnkle = Read_Angle(L_Ankle);

  // Print the angles to the serial in a format easy to parse in Python
  Serial.print(angleThigh);
  Serial.print(",");
  Serial.print(angleKnee);
  Serial.print(",");
  Serial.println(angleAnkle);

  delay(1000); // Delay for a second (adjust as needed)
}

float Read_Angle(float joint[7]) {
  // ... (Keep the Read_Angle function unchanged)
}

float fmap(float x, float in_min, float in_max, float out_min, float out_max) {
  // ... (Keep the fmap function unchanged)
}
