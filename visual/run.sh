DRIVER=chrome BASE_URL=http://testapp.galenframework.com galen test qa/visual/tests/ --jsonreport qa/visual/reports --config qa/visual/current_remote_chrome.config
DRIVER=firefox BASE_URL=http://testapp.galenframework.com galen test qa/visual/tests/ --jsonreport qa/visual/reports --config qa/visual/current_remote_firefox.config
behave qa/visual/features