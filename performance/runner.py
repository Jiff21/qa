import subprocess
from qa.accessibility.features.environment import FILE_NAME
from qa.settings import PAGES_LIST, BASE_URL, QA_FOLDER_PATH


generated_command = 'locust --clients=60 --hatch-rate=1 --num-request=200 \
        --no-web --csv=qa/performance/results/ \
        --host=https://example.com -f qa/performance/locustfile.py' % (
    QA_FOLDER_PATH,
    BASE_URL
)
process = subprocess.Popen(
    generated_command,
    stderr=subprocess.STDOUT,
    shell=True
)
process.wait()
