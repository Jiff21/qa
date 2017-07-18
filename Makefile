##############
# QA Additions
##############
qa_setup:
ifeq ("$(wildcard $(../.gitignore))","")
	echo 'gitignore exits in root adding QA ignores'
	echo '\n' >> ../.gitignore
	cat .gitignore >> ../.gitignore
else
	echo 'gignore does not exist, creating it in root'
	cat .gitignore > ../.gitignore
endif
ifeq ("$(wildcard $(../Makefile))","")
	echo 'Makefile exists copying QA commands into it'
	echo '\n' >> ../Makefile
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

zap_serve:
	. qa/env/bin/activate
	docker run -p 8090:8090 -i owasp/zap2docker-stable zap.sh -daemon -port 8090 -host 0.0.0.0 -config api.key=0123456789 -config api.addrs.addr.name=.* -config api.addrs.addr.regex=true -config scanner.strength=INSANE

test_all:
	source qa/env/bin/activate ;\
	python qa/accessibility/page_runner.py > qa/results/current_results.txt ;\
	behave qa/e2e/features >> qa/results/current_results.txt;\
	python qa/pen/zap_scanner.py >> qa/results/current_results.txt;\
	deactivate ;\
	source qa/locust_env/bin/activate ;\
	python qa/perf/runner.py ;\
	deactivate

##############
# QA Additions
##############
