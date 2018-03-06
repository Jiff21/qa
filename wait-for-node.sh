# RUn as follows below, passing in browser:version
# . qa/wait-for-node.sh chrome:64.0.3282.140



# Some variables stolen from wait-for.
TIMEOUT=60
QUIET=0

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

VERSION=$(echo $VERSION | sed s/[.]/[\.]/g)

BROWSER_REGEX=".browserName=$BROWSER_NAME,"
VERSION_REGEX=".version=$VERSION,"

printf "BROWSER_REGEX is %s\n" "$BROWSER_REGEX"
printf "The VERSION_REGEX is %s\n" "$VERSION_REGEX"

HUB_RESPONSE=$(curl http://localhost:4444/grid/console#)

if [[ $HUB_RESPONSE =~ $BROWSER_REGEX]] && [[$HUB_RESPONSE =~ $VERSION_REGEX ]]; then echo "BROWSER FOUND:\n%s" "${BASH_REMATCH[1]}"; fi
