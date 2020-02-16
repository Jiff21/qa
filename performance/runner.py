import os
import subprocess
from qa.settings import PAGES_DICT, HOST_URL, QA_FOLDER_PATH
from pathlib import Path

directory = '%s/performance/results/' % QA_FOLDER_PATH
if not os.path.exists(directory):
    os.makedirs(directory)

results_csv = '%s/performance/results/_requests.csv' % QA_FOLDER_PATH
if not os.path.isfile(results_csv):
    Path(results_csv).touch()

# 2190 requests in 3 minutes
generated_command = 'locust \
        -c 88 \
        -r 4 \
        -t 3m \
        --no-web \
        --csv=%s/performance/results/ \
        -H %s \
        -f %s/performance/locustfile.py' % (
            QA_FOLDER_PATH,
            HOST_URL,
            QA_FOLDER_PATH)
process = subprocess.Popen(
    generated_command,
    stderr=subprocess.STDOUT,
    shell=True
)
process.wait()

generated_command = 'HOST_URL=%s behave %s/performance/features' % (
    HOST_URL,
    QA_FOLDER_PATH
    )
process = subprocess.Popen(
    generated_command,
    stderr=subprocess.STDOUT,
    shell=True
)
process.wait()
