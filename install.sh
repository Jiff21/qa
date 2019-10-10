#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT=$(dirname ${DIR})
requiredver="3.6"

if ! [ -x "$(command -v virtualenv --version)" ]; then
  echo 'Error: virtualenv is not installed.\nPlease run pip3 install virtualenv' >&2
  return 1
fi


if ! [ -x "$(command -v docker --version)" ]; then
  echo 'Error: Docker is not installed.\nDonwload Docker C.E. and install from dmg file' >&2
  return 1
fi

install_functional_dependencies () {
  . qa/utilities/driver_update/geckodriver.sh
  . qa/utilities/driver_update/chromedriver.sh
  . qa/utilities/oauth/browsermob_install.sh
  pip3 install -U -r qa/functional/requirements.txt
  pip3 install -U -r qa/utilities/oauth/requirements.txt
  pip3 install -U -r qa/utilities/allure/requirements.txt
}


env_python="$(which python$requiredver)"
if [ "$(printf '%s\n' "$requiredver" "$env_python" | sort -V | head -n1)" = "$requiredver" ]; then
  echo "Python $requiredver installed. Checking for virtualenv"
  if [ ! -d qa/env ]; then
    echo "No virtualenv, creating and activating."
    virtualenv -p python$requiredver qa/env
    source qa/env/bin/activate
    install_functional_dependencies
  else
    echo "Env folder exists already. Activating virtualenv."
    source qa/env/bin/activate
    virtual_env_python="$(python --version)"
    echo "virtualenv python version is $virtual_env_python"
    if [ "$(printf '%s\n' "$requiredver" "$virtual_env_python" | sort -V | head -n1)" != "$requiredver" ]; then
      echo "Existing virtualenv has wrong version of python. Please delete it and run script again."
      deactivate
      return 1
    else
      install_functional_dependencies
    fi
  fi
else
  echo "Python $requiredver required. Please install it using dmg found at:\n https://www.python.org/downloads/"
  return 1
fi
