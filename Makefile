qa_setup:
ifneq ("$(wildcard $(../.gitignore))","")
	echo 'gitignore exits in root adding QA ignores'
	cat '\n\n' >> ../.gitignore
	cat .gitignore >> ../.gitignore
else
	echo 'gignore does not exist, creating it in root'
	cat .gitignore > ../.gitignore
endif
ifneq ("$(wildcard $(../Makefile))","")
	echo 'Makefile exists copying QA commands into it'
	cat '\n\n' >> ../Makefile
	cat Makefile >> ../Makefile
else
	echo 'Makefile does not exist copying QA commands into it'
	cat Makefile > ../Makefile
endif


# Run from inside qa file. Installs all dependencies.
qa_install:
	virtualenv -p python3 qa/env ;\
	source qa/env/bin/activate ;\
	pip install -r qa/e2e/requirements.txt ;\
	curl -L https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-macos.tar.gz | tar xz -C qa/env/bin ;\
	curl -L https://chromedriver.storage.googleapis.com/2.30/chromedriver_mac64.zip | tar xz -C qa/env/bin ;\
	pip install -r qa/pen/requirements.txt ;\
	pip install -r qa/accessibility/requirements.txt ;\
	deactivate ;\
	virtualenv -p python2.7 qa/locust_env ;\
	source qa/locust_env/bin/activate ;\
	pip install -r qa/perf/requirements.txt ;\
	deactivate

.PHONY: test_all
test_all: test

.PHONY: test_unit
test_unit:
	tox
