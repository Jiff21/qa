import os
import re
import subprocess
from qa.settings import PAGES_DICT, HOST_URL, QA_FOLDER_PATH
from pathlib import Path
from qa.functional.features.steps.custom_exceptions import loop_thru_messages


BANDIT_EXCLUDES='B308,B101'


def check_results(path, exclude):
    generated_command = 'bandit -r --skip="%s" %s' % (
                exclude,
                path,
    )
    process = subprocess.Popen(
        generated_command,
        stdout=subprocess.PIPE,
        shell=True
    )
    process.wait()
    return process.communicate()[0]


@step('I scan "{file_path}" with bandit')
def step_impl(context, file_path):
    context.scan_results = check_results(file_path, BANDIT_EXCLUDES)


@step('the bandit scan should not contain any "{severity}" severity issues')
def step_impl(context, severity):
    search_regex = '%s: (\d+.\d+)' % severity
    match = re.search(search_regex, str(context.scan_results))
    assert match is not None, 'Did not get a match from these results:\n%s' % context.scan_results
    assert float(match.group(1)) == 0, 'Found %s %s issues' % (str(match.group(1)), severity)
