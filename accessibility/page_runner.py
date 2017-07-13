import subprocess
from environment_variables import PAGES_LIST, BASE_URL, QA_FOLDER_PATH


def generated_command(root_folder_path, report_name, base_url, uri):
    generated_command = 'docker run \
        -v $PWD/%saccessibility/output/:/lighthouse/output/  \
        -i matthiaswinkelmann/lighthouse-chromium-alpine \
        --output json --output html \
        --output-path=/lighthouse/output%s %s%s' % (
        QA_FOLDER_PATH,
        page,
        BASE_URL,
        page


for page in PAGES_LIST:
    generated_command=''
    if page == '/':
        generated_command='docker run \
            -v $PWD/%saccessibility/output/:/lighthouse/output/  \
            -i matthiaswinkelmann/lighthouse-chromium-alpine \
            --output json --output html \
            --output-path=/lighthouse/output/index %s%s' % (
            QA_FOLDER_PATH,
            BASE_URL,
            page
        )
    else:
        generated_command='docker run \
            -v $PWD/%saccessibility/output/:/lighthouse/output/  \
            -i matthiaswinkelmann/lighthouse-chromium-alpine \
            --output json --output html \
            --output-path=/lighthouse/output%s %s%s' % (
            QA_FOLDER_PATH,
            page,
            BASE_URL,
            page
        )

    process=subprocess.Popen(
        generated_command,
        stderr=subprocess.STDOUT,
        shell=True
    )
    process.wait()


for page in PAGES_LIST:
    generated_command=''
    if page == '/':
        generated_command='FILE_NAME=%s behave accessibility/features' % (
            'index'
        )
    else:
        generated_command='FILE_NAME=%s behave accessibility/features' % (
            page.replace('/', '')
        )
    process=subprocess.Popen(
        generated_command,
        stderr=subprocess.STDOUT,
        shell=True
    )
    process.wait()
