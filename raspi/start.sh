sudo python3 -m http.server --bind raspberrypi.local 80 &
python3 ws_server.py &
python3 dimmer.py &

wait
