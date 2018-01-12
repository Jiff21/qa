##############
# QA Additions
##############

# Run from inside qa file. Installs all dependencies.
qa_install:
	virtualenv -p python3 qa/env ;\
	source qa/env/bin/activate ;\
	pip install -r qa/functional/requirements.txt ;\
	cp qa/functional/behave.ini . ;\
	curl -L https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-macos.tar.gz | tar xz -C qa/env/bin ;\
	. qa/utilities/driver_update/chromedriver.sh ;\
	cp qa/analytics/ga_tracker.crx qa/env/bin ;\
	pip install -r qa/security/requirements.txt ;\
	pip install -r qa/analytics/requirements.txt ;\
	pip install -r qa/visual/requirements.txt ;\
	pip install -r qa/accessibility/requirements.txt ;\
	deactivate ;\
	virtualenv -p python2.7 qa/pytwo_env ;\
	source qa/pytwo_env/bin/activate ;\
	pip install -r qa/utilities/oauth/requirements.txt ;\
	pip install -r qa/performance/requirements.txt ;\
	deactivate

zap_up:
	. qa/env/bin/activate
	docker run -p 8081:8081 -i owasp/zap2docker-stable zap.sh -daemon -port 8081 -host 0.0.0.0 -config api.key=0123456789 -config api.addrs.addr.name=.* -config api.addrs.addr.regex=true -config scanner.strength=INSANE

lighthouse_up:
	. qa/env/bin/activate
	docker run -p 8085:8085 kmturley/lighthouse-ci


test_all:
	source qa/env/bin/activate ;\
	python qa/accessibility/page_runner.py > qa/results/current_results.txt ;\
	behave qa/functional/features >> qa/results/current_results.txt;\
	python qa/security/zap_scanner.py >> qa/results/current_results.txt;\
	DRIVER=ga_chrome behave qa/analytics/features >> qa/results/current_results.txt;\
	# behave qa/visual/features >> qa/results/current_results.txt;\
	deactivate ;\
	source qa/pytwo_env/bin/activate ;\
	python qa/performance/runner.py ;\
	deactivate

##############
# QA Additions
##############
