#!/bin/bash

# sudo apt-get install cpufrequtils if not already present

if [ $(dpkg-query -W -f='${Status}' cpufrequtils 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  apt install cpufrequtils;
else
    echo "cpufrequtils requirement already statisfied"
fi

