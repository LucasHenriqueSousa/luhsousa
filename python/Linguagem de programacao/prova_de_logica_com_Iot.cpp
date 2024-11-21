// C++ code
//
void setup()
{
  pinMode(4, INPUT);
  pinMode(3, INPUT);
  pinMode(2, INPUT);
  pinMode(1, INPUT);
  pinMode(0, INPUT);
  pinMode(6, INPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop()
{
  if (digitalRead(4) == 0) {
    if (((digitalRead(3) == 0 || (digitalRead(2) == 0 || digitalRead(1) == 0)) || digitalRead(0) == 0) && digitalRead(6) == 1) {
      digitalWrite(11, HIGH);
      delay(1000); // Wait for 1000 millisecond(s)
      digitalWrite(11, LOW);
      delay(1000); // Wait for 1000 millisecond(s)
      digitalWrite(12, HIGH);
      delay(1000); // Wait for 1000 millisecond(s)
      digitalWrite(12, LOW);
      delay(1000); // Wait for 1000 millisecond(s)
    } else {
      if (((digitalRead(3) == 0 || (digitalRead(2) == 0 || digitalRead(1) == 0)) || digitalRead(0) == 0) && digitalRead(6) == 0) {
        digitalWrite(11, LOW);
        digitalWrite(12, LOW);
        digitalWrite(13, HIGH);
        delay(2); // Wait for 2 millisecond(s)
        digitalWrite(13, LOW);
        delay(2); // Wait for 2 millisecond(s)
      } else {
        if (((digitalRead(3) == 1 || (digitalRead(2) == 1 || digitalRead(1) == 1)) || digitalRead(0) == 1) && digitalRead(6) == 0) {
          digitalWrite(11, HIGH);
          digitalWrite(12, HIGH);
          digitalWrite(13, HIGH);
          delay(1.5); // Wait for 1.5 millisecond(s)
          digitalWrite(13, LOW);
          delay(1.5); // Wait for 1.5 millisecond(s)
        }
      }
    }
  } else {
    digitalWrite(13, LOW);
    digitalWrite(11, LOW);
    digitalWrite(12, LOW);
  }