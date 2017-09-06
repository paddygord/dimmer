#!/bin/bash

BLUEZCARD=`pactl list cards short | egrep -o bluez.*[[:space:]]`
pactl set-card-profile $BLUEZCARD a2dp_source
#pactl set-card-profile $BLUEZCARD off
pactl set-card-profile $BLUEZCARD a2dp_source

pactl unload-module module-loopback
pactl load-module module-loopback source=bluez_source.5C_F3_70_83_61_D3.a2dp_source sink=alsa_output.platform-soc_audio.analog-stereo
