unsigned char channel_0 = 7;
unsigned char channel_1 = 6;
unsigned char dimming_0 = 0;
unsigned char dimming_1 = 0;
unsigned char buf[3] = {0, 0};
void zero_cross() {
    delayMicroseconds(100 * constrain(dimming_0, 10, 85));
    digitalWrite(channel_0, HIGH);
    digitalWrite(channel_1, HIGH);
    delayMicroseconds(10);
    digitalWrite(channel_0, LOW);
    digitalWrite(channel_1, LOW);
}
void setup() {
    Serial.begin(9600);
    pinMode(channel_0, OUTPUT);
    pinMode(channel_1, OUTPUT);
    attachInterrupt(digitalPinToInterrupt(3), zero_cross, RISING);
}
void loop() {
    while (Serial.peek() != 116) {
        Serial.read();
        return;
    }
    while (Serial.available() < sizeof(buf)) {
        return;
    }
    if (Serial.readBytes(buf, sizeof(buf)) != sizeof(buf))
        return;
    if (buf[1] > 100 || buf[2] > 100)
        return;
    dimming_0 = buf[1];
    dimming_1 = buf[2];
    Serial.print(buf[1]);
    Serial.print(' ');
    Serial.println(buf[2]);
    //dimming_0 = 50 + 50 * sin((float)millis() / 1000);
}
