unsigned char channel_0 = 7;
unsigned char channel_1 = 6;
unsigned char dimming_0 = 0;
unsigned char dimming_1 = 0;
void zero_cross() {
    delayMicroseconds(100 * constrain(dimming_0, 5, 85));
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
    unsigned char buf[3];
    if (Serial.available() < sizeof(buf))
        return;
    int num = Serial.readBytesUntil(127, buf, sizeof(buf));
    if (num != sizeof(buf))
        return;
    if (buf[0] > 100 || buf[1] > 100)
        return;
    dimming_0 = buf[0];
    dimming_1 = buf[1];
    Serial.print(buf[0]);
    Serial.print(' ');
    Serial.println(buf[1]);
    //dimming_0 = 50 + 50 * sin((float)millis() / 1000);
}
