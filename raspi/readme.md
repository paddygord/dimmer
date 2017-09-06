# Raspberry Pi Fairy Light Controller

## Dependencies

```
sudo apt install python3 python3-pip
pip3 install rpi.gpio
```
## Run

```
python3 dimmer.py
```
if this doesn't work, you may need to add your user to the gpio group and check the permissions are correct, see [here](https://raspberrypi.stackexchange.com/questions/40105/access-gpio-pins-without-root-no-access-to-dev-mem-try-running-as-root)


uses mDNS to broadcast a .local domain name, by default raspberrypi.local
android doesn't support mDNS, so you'll have to find the IP address manually


bluetooth setup
various config file settings
computer:
`/etc/bluetooth/main.conf` append line `AutoEnable=true`

raspberrypi:
`/etc/bluetooth/main.conf`
append `[General]
Name = raspberrypi
Class = 0x20041c`
`AutoEnable=true`

`/etc/bluetooth/audio.conf`
`[General]
Class = 0x20041c
Enable = Source,Sink,Media


sudo bluetoothctl
power on
agent on
default-agent
discoverable on
scan on
pair ...
trust ...
connect ...
exit


pulseaudio setup
`/etc/pulse/default.pa`
load-module module-switch-on-connect

`/etc/pulse/daemon.conf`
`resample-method=trivial`


`pactl load-module module-loopback source=bluez_source.5C_F3_70_83_61_D3.a2dp_source sink=alsa_output.platform-soc_audio.analog-stereo`
