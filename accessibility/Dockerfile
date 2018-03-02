FROM alpine:3.6

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
  tar \
  unzip\
  wget


RUN mkdir /usr/tmp
COPY qa/functional/requirements.txt /usr/tmp/functional_requirements.txt
COPY qa/accessibility/requirements.txt /usr/tmp/accessibility_requirements.txt
COPY qa/analytics/requirements.txt /usr/tmp/analytics_requirements.txt
COPY qa/performance/requirements.txt /usr/tmp/performance_requirements.txt
COPY qa/security/requirements.txt /usr/tmp/security_requirements.txt
COPY qa/utilities/oauth/requirements.txt /usr/tmp/oauth_requirements.txt



RUN pip3 install --upgrade pip setuptools
RUN pip3 install -r /usr/tmp/functional_requirements.txt
RUN pip3 install -r /usr/tmp/accessibility_requirements.txt
RUN pip3 install -r /usr/tmp/analytics_requirements.txt
RUN pip3 install -r /usr/tmp/performance_requirements.txt
RUN pip3 install -r /usr/tmp/security_requirements.txt
RUN pip3 install -r /usr/tmp/oauth_requirements.txt

COPY qa/functional /usr/tmp/



CMD /bin/bash
