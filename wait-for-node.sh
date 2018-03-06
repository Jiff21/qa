# RUn as follows below, passing in browser:version
# . qa/wait-for-node.sh chrome:64.0.3282.140



# Some variables stolen from wait-for.
TIMEOUT=60
QUIET=0
SELENIUM_ADDRESS='http://localhost:4444'


usage() {
  exitcode="$1"
  cat << USAGE >&2
Usage:
  $cmdname browsername:version [-t timeout] [-- command args]
  -q | --quiet                        Do not output any status messages
  -t TIMEOUT | --timeout=timeout      Timeout in seconds, zero for no timeout
  -- COMMAND ARGS                     Execute command with args after the test finishes
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
    -t)
    TIMEOUT="$2"
    if [ "$TIMEOUT" = "" ]; then break; fi
    shift 2
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

printf "BROWSER_NAME is %s\n" "$BROWSER_NAME"
printf "The VERSION is %s\n" "$VERSION"

VERSION=$(echo $VERSION | sed s/[.]/\\\\./g)

BROWSER_REGEX=".browserName=$BROWSER_NAME,"
VERSION_REGEX=".version=$VERSION,"

printf "BROWSER_REGEX is %s\n" "$BROWSER_REGEX"
printf "The VERSION_REGEX is %s\n" "$VERSION_REGEX"

# if [[ $HUB_RESPONSE =~ $VERSION_REGEX && $HUB_RESPONSE =~ $BROWSER_REGEX  ]]; then echo "BROWSER FOUND:\n%s" "${BASH_REMATCH[1]}"; fi
# HUB_RESPONSE=$(curl $SELENIUM_ADDRESS/grid/console#)
#if [[ $HUB_RESPONSE =~ $VERSION_REGEX && $HUB_RESPONSE =~ $BROWSER_REGEX  ]];
#then
#  echo "Browser and Version match found"
#else
#  echo "Did not find a match for both browser and version."
#fi

wait_for() {
  for i in `seq $TIMEOUT` ; do
    HUB_RESPONSE=$(curl $SELENIUM_ADDRESS/grid/console#)

    #result=$?
    if [[ $HUB_RESPONSE =~ $VERSION_REGEX && $HUB_RESPONSE =~ $BROWSER_REGEX  ]]; then
      if [ $# -gt 0 ] ; then
        exec "$@"
      fi
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
