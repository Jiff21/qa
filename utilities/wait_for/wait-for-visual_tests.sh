#!/bin/bash
# wait-for-postgres.sh
#
# set -e
# first_host='http://visual_current_firefox'
# second_host='http://visual_last_firefox'
# third_host='http://visual_current_firefox'
# fourth_host='http://visual_current_chrome'
#
#
# until curl -f $first_host; do
#   >&2 echo "Current Chrome still running"
#   sleep 1
# done
#
# >&2 echo "Current Chrome done"
# exec $cmd

if [docker inspect ballzstack_visual_current_chrome_1  --format='{{.State.ExitCode}}' && docker inspect ballzstack_visual_current_firefox_1  --format='{{.State.ExitCode}}'] == 0; then
  echo 'yes'


  if [docker inspect ballzstack_visual_current_chrome_1  --format='{{.State.ExitCode}}' == 0] ; then
    echo "yes"
  fi

until x > 0; do
  chome_current=${docker inspect ballzstack_visual_current_chrome_1  --format="{{.State.ExitCode}}"}
  >&2 echo "Current Chrome still running"
  sleep 1
done
