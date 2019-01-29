#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT=$(dirname ${DIR})
requiredver="3.4.0"

if ! [ -x "$(command -v virtualenv --version)" ]; then
  echo 'Error: virtualenv is not installed.\nPlease run pip3 install virtualenv' >&2
  return 1
fi

python3ver="$(python3 --version)"
if [! "$(printf '%s\n' "$requiredver" "$python3ver" | sort -V | head -n1)" = "$requiredver" ]; then
  echo "System python3 greater than $requiredver. Good there."
else
  echo "Less than $requiredver"
  return 1
fi


if ! [ -x "$(command -v docker --version)" ]; then
  echo 'Error: Docker is not installed.\nDonwload Docker C.E. and install from dmg file' >&2
  return 1
fi

if [ ! -d qa/env ]; then
  virtualenv -p python3.6 qa/env
  source qa/env/bin/activate
else
  source qa/env/bin/activate
  env_python="$(python --version)"
  if [ "$(printf '%s\n' "$requiredver" "$env_python" | sort -V | head -n1)" = "$requiredver" ]; then
    echo "Greater than or equal to $requiredver"
  else
    echo "Less than $requiredver"
    return 1
  fi
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
