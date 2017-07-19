import subprocess
from qa.accessibility.features.environment import FILE_NAME
from qa.environment_variables import PAGES_LIST, BASE_URL, QA_FOLDER_PATH


generated_command = 'locust --clients=2 --hatch-rate=1 --num-request=4 --no-web\
    -f %sperf/locustfile.py --host=%s >> qa/results/current_results.txt' % (
    QA_FOLDER_PATH,
    BASE_URL
)
process = subprocess.Popen(
    generated_command,
    stderr=subprocess.STDOUT,
    shell=True
)
process.wait()
