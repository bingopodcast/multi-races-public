#!/bin/bash

export DISPLAY=:0

killall -9 feh
feh --hide-pointer -F /home/pi/instruction_cards/$1.png &
