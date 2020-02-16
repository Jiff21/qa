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

# Suggested non demo settings
# -c = clients | -r = hatch rate | -h = host | -t = runtime
generated_command = 'locust -c 5 -r 10 -t 3m \
        --no-web --csv=%s/performance/results/ \
        -h %s -f %s/performance/locustfile.py' % (
            QA_FOLDER_PATH,
            HOST_URL,
            QA_FOLDER_PATH)
print(generated_command)
process = subprocess.Popen(
    generated_command,
    stderr=subprocess.STDOUT,
    shell=True
)
process.wait()
