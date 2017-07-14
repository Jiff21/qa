
setup:
	ifneq ("$(wildcard $(../.gitignore))","")
		.gitignore > '\n\n'
		.gitignore > .gitignore
	else
		cp .gitignore ../
	endif

# if [ -a .gitignore ] ; \
# then \
# 	.gitignore > ../.gitignore
# else \
# 	cp .gitignore ../
# fi \

qa_install:
	virtualenv -p python3 env ;\
	source env/bin/activate ;\
	pip install -r e2e/requirements.txt ;\
	curl -L https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-macos.tar.gz | tar xz -C qa/env/bin ;\
	curl -L https://chromedriver.storage.googleapis.com/2.30/chromedriver_mac64.zip | tar xz -C qa/env/bin ;\
	pip install -r pen/requirements.txt ;\
	pip install -r accessibility/requirements.txt ;\
	deactivate ;\
	virtualenv -p python2.7 locust_env ;\
	source locust_env/bin/activate ;\
	pip install -r perf/requirements.txt ;\
	deactivate

.PHONY: test_all
test_all: test

.PHONY: test_unit
test_unit:
	tox
