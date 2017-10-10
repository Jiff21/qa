import subprocess
from qa.accessibility.features.environment import FILE_NAME
from qa.settings import PAGES_LIST, BASE_URL, QA_FOLDER_PATH

directory = '%s/performance/results/' % QA_FOLDER_PATH
if not os.path.exists(directory):
    os.makedirs(directory)

generated_command = 'locust --clients=3 --hatch-rate=1 --num-request=6 \
        --no-web --csv=%s/performance/results/ \
        --host=%s -f %s/performance/locustfile.py' % (
            QA_FOLDER_PATH,
            BASE_URL,
            QA_FOLDER_PATH)
process = subprocess.Popen(
    generated_command,
    stderr=subprocess.STDOUT,
    shell=True
)
process.wait()

generated_command = 'BASE_URL=%s behave %s/performance/features' % (
    BASE_URL,
    QA_FOLDER_PATH
    )
process = subprocess.Popen(
    generated_command,
    stderr=subprocess.STDOUT,
    shell=True
)
process.wait()
