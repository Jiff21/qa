FROM alpine:3.6

ENV PYTHONPATH="$PYTHONPATH:/usr/lib/python3.5"
ENV GALEN_VERSION=2.3.6

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
  openjdk8-jre\
  openssh-client\
  python3\
  python3-dev\
  tar \
  unzip\
  wget \
  zeromq-dev


# Galen install
RUN wget https://github.com/galenframework/galen/releases/download/galen-$GALEN_VERSION/galen-bin-$GALEN_VERSION.zip \
  && unzip galen-bin-$GALEN_VERSION \
  && cd galen-bin-$GALEN_VERSION \
  && chmod +x install.sh \
  && . install.sh \
  && cd ..

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
  && mkdir /usr/tmp/utilities/allure/allure_results

COPY functional/requirements.txt /usr/tmp/functional_requirements.txt
COPY accessibility/requirements.txt /usr/tmp/accessibility_requirements.txt
COPY analytics/requirements.txt /usr/tmp/analytics_requirements.txt
COPY performance/requirements.txt /usr/tmp/performance_requirements.txt
COPY visual/requirements.txt /usr/tmp/visual_requirements.txt
COPY security/requirements.txt /usr/tmp/security_requirements.txt
COPY utilities/oauth/requirements.txt /usr/tmp/oauth_requirements.txt
COPY utilities/allure/requirements.txt /usr/tmp/allure_requirements.txt

RUN pip3 install --upgrade pip setuptools
RUN pip3 install -r /usr/tmp/functional_requirements.txt
RUN pip3 install -r /usr/tmp/accessibility_requirements.txt
RUN pip3 install -r /usr/tmp/analytics_requirements.txt
RUN pip3 install -r /usr/tmp/performance_requirements.txt
RUN pip3 install -r /usr/tmp/visual_requirements.txt
RUN pip3 install -r /usr/tmp/security_requirements.txt
RUN pip3 install -r /usr/tmp/oauth_requirements.txt
RUN pip3 install -r /usr/tmp/allure_requirements.txt

COPY utilities/oauth/browsermob_install.sh /usr/tmp/browsermob_install.sh
RUN ./usr/tmp/browsermob_install.sh

RUN touch /usr/tmp/__init__.py
COPY . /usr/tmp/qa
WORKDIR /usr/tmp
RUN chmod +x qa/utilities/wait_for/wait-for-node.sh

CMD ["/bin/bash"]
