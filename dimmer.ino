unsigned char channel_1 = 7;
unsigned char channel_2 = 6;
unsigned char dimming = 0;
unsigned char flag = 0;
void zero_cross_int() {
    int dimtime = (100 * dimming);
    delayMicroseconds(dimtime);
    if (flag) {
        digitalWrite(channel_1, HIGH);
        delayMicroseconds(10);
        digitalWrite(channel_1, LOW);
    } else {
        digitalWrite(channel_2, HIGH);
        delayMicroseconds(10);
        digitalWrite(channel_2, LOW);
    }
}
void setup() {
    pinMode(channel_1, OUTPUT);
    pinMode(channel_2, OUTPUT);
    attachInterrupt(1, zero_cross_int, RISING);
}
void loop() {
    unsigned char i;
    for (i = 100; i > 0; i--){
        dimming = i;
        delay(20);
    }

    for (i = 0; i < 100; i++) {
        dimming = i;
        delay(20);
    }
    flag = ~flag;
}
