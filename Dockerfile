FROM alpine:3.4

# Extend alpine with basic tools
RUN apk --update --no-cache add\
  alpine-sdk\
  autoconf \
  automake \
  bash\
  build-base\
  curl\
  git\
  gzip \
  jpeg\
  jpeg-dev\
  libffi\
  libffi-dev\
  libpng \
  libpng-dev\
  libtool \
  mysql\
  mysql-client\
  mysql-dev\
  nasm\
  nodejs\
  openjdk7-jre\
  openssh-client\
  python3\
  python3-dev\
  tar \
  unzip\
  wget


RUN mkdir /usr/tmp \
  && mkdir /usr/tmp/qa \
  && mkdir /usr/tmp/qa/functional \
  && mkdir /usr/tmp/qa/accessibility \
  && mkdir /usr/tmp/qa/analytics \
  && mkdir /usr/tmp/qa/performance \
  && mkdir /usr/tmp/qa/security \
  && mkdir /usr/tmp/utilities \
  && mkdir /usr/tmp/utilities/driver_update \
  && mkdir /usr/tmp/utilities/allure \
  && mkdir /usr/tmp/utilities/allure/allure_result_folder

COPY functional/requirements.txt /usr/tmp/functional_requirements.txt
COPY accessibility/requirements.txt /usr/tmp/accessibility_requirements.txt
COPY analytics/requirements.txt /usr/tmp/analytics_requirements.txt
COPY performance/requirements.txt /usr/tmp/performance_requirements.txt
COPY security/requirements.txt /usr/tmp/security_requirements.txt
COPY utilities/oauth/requirements.txt /usr/tmp/oauth_requirements.txt
COPY utilities/allure/requirements.txt /usr/tmp/allure_requirements.txt

RUN pip3 install --upgrade pip setuptools
RUN pip3 install -r /usr/tmp/functional_requirements.txt
RUN pip3 install -r /usr/tmp/accessibility_requirements.txt
RUN pip3 install -r /usr/tmp/analytics_requirements.txt
RUN pip3 install -r /usr/tmp/performance_requirements.txt
RUN pip3 install -r /usr/tmp/security_requirements.txt
RUN pip3 install -r /usr/tmp/oauth_requirements.txt
RUN pip3 install -r /usr/tmp/allure_requirements.txt

COPY . /usr/tmp/qa
WORKDIR /usr/tmp

#CMD BASE_URL=https://google.com DRIVER=headless_chrome SELENIUM=http://selenium_hub:4444/wd/hub behave -f allure_behave.formatter:AllureFormatter -o qa/utilities/allure/allure_result_folder ./qa/functional/features -i google
ENTRYPOINT ["/bin/bash"]
