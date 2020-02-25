#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT=$(dirname ${DIR})
requiredver="3.4"
first_untested_python='3.8.2'



# Python version checks
python3ver="$(python3 --version | tr -d 'Python ')"
if ! [ -x "$(command -v python3 --version )" ]; then
  echo 'Python 3 not installed' >&2
  exit 1
fi
# Check Python is new enough
if [ "$(printf '%s\n' "$requiredver" "$python3ver" | sort -V | head -n1)" = "$requiredver" ]; then
  echo "User has Python $python3ver, which meets > $requiredver requirement."
else
  echo "Less than $requiredver"
  exit 1
fi
# Warn if Pythhon is newer than tested
if [ "$(printf '%s\n' "$first_untested_python" "$python3ver" | sort -V | head -n1)" = "$first_untested_python" ]; then
  printf "\n\nWARNING:Has not been tested above Python $first_untested_python may or may not work.\n\n'."
fi
# Check virtualenv installed
if ! [ -x "$(command -v virtualenv --version)" ]; then
  printf 'virtualenv is not installed.\Running pip3 install virtualenv.\n'
  pip3 install virtualenv
fi

# Docker version check
if ! [ -x "$(command -v docker --version)" ]; then
  echo 'Error: Docker is not installed.\nDonwload Docker C.E. and install from dmg file' >&2
  exit 1
fi

if [[ -d qa/env ]]; then
  echo "virtualenv exists checking version"
  source qa/env/bin/activate
  env_python="$(python --version)"
  if [ "$(printf '%s\n' "$requiredver" "$env_python" | sort -V | head -n1)" = "$requiredver" ]; then
    echo "Existing virtualenv using Python $env_python, meets > $requiredver requirement."
  else
    echo "Less than $requiredver"
    exit 1
  fi
else
  echo "creating virtualenv"
  virtualenv -p python3 qa/env
  source qa/env/bin/activate
fi



. qa/utilities/driver_update/geckodriver.sh
. qa/utilities/driver_update/chromedriver.sh
cp qa/analytics/ga_tracker.crx qa/env/bin
pip3 install -U -r qa/functional/requirements.txt
pip3 install -U -r qa/security/requirements.txt
pip3 install -U -r qa/analytics/requirements.txt
pip3 install -U -r qa/visual/requirements.txt
pip3 install -U -r qa/accessibility/requirements.txt
pip3 install -U -r qa/performance/requirements.txt
pip3 install -U -r qa/utilities/oauth/requirements.txt
pip3 install -U -r qa/utilities/allure/requirements.txt
curl -L https://github.com/galenframework/galen/releases/download/galen-2.3.6/galen-bin-2.3.6.zip | tar xy -C qa/env/bin/
cd qa/env/bin/galen-bin-2.3.6 && sudo ./install.sh && cd ../../../../

source qa/env/bin/activate
