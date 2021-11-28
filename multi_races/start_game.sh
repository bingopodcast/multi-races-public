#!/bin/bash

cd /home/nbaldridge/proc/multi-races/multi_races

killall -9 python
python menu.py $1
