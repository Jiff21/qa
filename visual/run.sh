DRIVER=chrome BASE_URL=${1} galen test qa/visual/tests/ --jsonreport qa/visual/reports --config qa/visual/current_remote_chrome.config
DRIVER=firefox BASE_URL=${1} galen test qa/visual/tests/ --jsonreport qa/visual/reports --config qa/visual/current_remote_firefox.config
behave qa/visual/features
