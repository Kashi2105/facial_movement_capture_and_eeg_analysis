void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);  // Initialize serial communication
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n'); // Read the incoming data until newline character
    if (data == "turn_on_led") { // Check if received data is "turn_on_led"
      digitalWrite(13, HIGH); // Turn on LED connected to pin 13
      Serial.println("LED turned on"); // Send acknowledgment back to Python server
    }
    if (data == "turn_off_led") { // Check if received data is "turn_on_led"
      digitalWrite(13, LOW); // Turn on LED connected to pin 13
      Serial.println("LED turned off"); // Send acknowledgment back to Python server
    }
  }
}
