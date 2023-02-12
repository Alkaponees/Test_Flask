#!/bin/bash
while :
do 
  # Get the current usage of CPU and memory
  cpuUsage=$(top -bn1 | awk '/Cpu/ { print $2}')
  memUsage=$(free -m | awk '/Mem/{print $3}')
  curl  -H 'Content-Type: application/json' --data "{"CPU_Usage":"${cpuUsage}"),"Memory_Usage":"${memUsage}"}"  http://loclahost:8080/test
  echo "CPU Usage: $cpuUsage%"
  echo "Memory Usage: $memUsage MB"
 
  # Sleep for 1 second
  sleep 1
done