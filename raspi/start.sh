#!/bin/bash
cd /home/pi/fairy-light-controller/raspi
sudo python3 -m http.server --bind raspberrypi.local 80 &
python3 ws_server.py &
sudo nice -n -5 python3 dimmer.py &

wait
