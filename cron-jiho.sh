#!/bin/bash

export PULSE_SERVER=tcp:$(grep nameserver /etc/resolv.conf | awk '{print $2}')
script_path=$HOME

python3 ${script_path}/main.py > /tmp/cron-jiho.log 2>&1
