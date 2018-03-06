# RUn as follows below, passing in browser:version
# . qa/wait-for-node.sh chrome:64.0.3282.140



# Some variables stolen from wait-for.
TIMEOUT=60
QUIET=0
SELENIUM_ADDRESS='http://localhost:4444'
# Need to add a way to feed this from command line for docker.

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

printf "Looking for %s browser.\n" "$BROWSER_NAME"
printf "Version: %s\n" "$VERSION"

VERSION=$(echo $VERSION | sed s/[.]/\\\\./g)

BROWSER_REGEX=".browserName=$BROWSER_NAME,"
VERSION_REGEX=".version=$VERSION,"

wait_for() {
  for i in `seq $TIMEOUT` ; do
    echo "Getting Hub response"
    HUB_RESPONSE=$(curl $SELENIUM_ADDRESS/grid/console#)

    echo "Checking response for version and browser."
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
