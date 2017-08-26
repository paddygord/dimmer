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
