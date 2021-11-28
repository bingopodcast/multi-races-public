#!/bin/bash

sshpass -p raspberry ssh pi@10.0.0.51 sudo halt
sshpass -p raspberry ssh pi@10.0.0.52 sudo halt

#shutdown -h now
