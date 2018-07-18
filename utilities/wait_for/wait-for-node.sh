#!/bin/bash

# Run as follows below, mandatory is to include browser:version
# . qa/utilities/wait_for/wait-for-node.sh chrome:64.0.3282.140

# Set default values for optional variables.
TIMEOUT=60
QUIET=0
SELENIUM_ADDRESS='localhost'
SELENIUM_PORT='4444'

usage() {
  exitcode="$1"
  cat << USAGE >&2
Usage:
  $cmdname browsername:version [-s address] [-p address]  [--timeout=##] [-- command args]
  -q | --quiet                                          Do not output any status messages
  -s address | --selenium_hub=0.0.0.0                   Address for Selenium hub after http://
  -p #### | --port=4444                                 Port for selenium hub
  --timeout=##                                          Timeout in seconds, zero for no timeout
  -- COMMAND ARGS                                       Execute command with args after the test finishes
USAGE
  exit "$exitcode"
}


while [ $# -gt 0 ]
do
  case "$1" in
    *:* )
    BROWSER_NAME=$(printf "%s\n" "$1"| cut -d : -f 1)
    VERSION=$(printf "%s\n" "$1"| cut -d : -f 2)
    shift 1
    ;;
    -q | --quiet)
    QUIET=1
    shift 1
    ;;
    -s)
    SELENIUM_ADDRESS="$2"
    if [ "$SELENIUM_ADDRESS" = "" ]; then break; fi
    shift 2
    ;;
    --selenium_hub=*)
    SELENIUM_ADDRESS="${1#*=}"
    shift 1
    ;;
    -p)
    SELENIUM_PORT="$2"
    if [ "$SELENIUM_ADDRESS" = "" ]; then break; fi
    shift 2
    ;;
    --port=*)
    SELENIUM_PORT="${1#*=}"
    shift 1
    ;;
    --timeout=*)
    TIMEOUT="${1#*=}"
    shift 1
    ;;
    --)
    shift
    break
    ;;
    --help)
    usage 0
    ;;
    *)
    echoerr "Unknown argument: $1"
    usage 1
    ;;
  esac
done

VERSION="$(echo $VERSION | sed s/[.]/\\\\./g)"

BROWSER_REGEX=".browserName=$BROWSER_NAME,"
VERSION_REGEX=".version=$VERSION,"

wait_for() {
  printf "Looking for %s browser.\n" "$BROWSER_NAME"
  printf "Version: %s\n" "$VERSION"
  printf "On a Selenium hub at %s\n" "http://$SELENIUM_ADDRESS:$SELENIUM_PORT/grid/console"
  for i in `seq $TIMEOUT` ; do
    echo "Getting Hub response"
    HUB_RESPONSE="$(curl http://$SELENIUM_ADDRESS:$SELENIUM_PORT/grid/console)"

    echo "Checking response for version and browser."
    if [[ $HUB_RESPONSE =~ $VERSION_REGEX && $HUB_RESPONSE =~ $BROWSER_REGEX  ]]; then
      echo "Browser found!"
      if [ $# -gt 0 ] ; then
        exec "$@"
      fi
      echo "No following command passed in."
      exit 0
    fi
    sleep 1
  done
  echo "Operation timed out" >&2
  exit 1
}


if [ "$BROWSER_REGEX" = "" -o "$VERSION_REGEX" = "" ]; then
  echoerr "Error: you need to provide a Browser and Version (e.g. chrome:63.0.1)."
  usage 2
fi

wait_for "$@"
